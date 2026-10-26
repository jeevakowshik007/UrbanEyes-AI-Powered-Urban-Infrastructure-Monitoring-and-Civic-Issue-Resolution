"""Storage abstraction: local filesystem (dev) or S3-compatible (prod/MinIO).

- Secure object paths: uuid prefix + sanitized basename (no traversal possible).
- Credentials never leave the server; clients get short-lived presigned URLs (S3)
  or authenticated streaming downloads (local) via the /files endpoint.
- Legacy STORAGE_BACKEND env is honored when STORAGE_PROVIDER is unset.
"""
from __future__ import annotations

import os
import re
import uuid
from abc import ABC, abstractmethod
from pathlib import Path

from app.core.config import get_settings
from app.core.logging import get_logger

log = get_logger("storage")

_KEY_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_./\-]{0,400}$")


def is_safe_key(key: str) -> bool:
    return bool(_KEY_RE.match(key or "")) and ".." not in (key or "").split("/")


def _secure_key(prefix: str, filename: str) -> str:
    base = os.path.basename(filename or "upload").strip() or "upload"
    base = re.sub(r"[^A-Za-z0-9_.\-]+", "_", base)[:120]
    clean_prefix = re.sub(r"[^A-Za-z0-9_\-]+", "_", prefix or "misc").strip("_") or "misc"
    return f"{clean_prefix}/{uuid.uuid4().hex}_{base}"


def sniff_image(data: bytes) -> str | None:
    """Magic-byte check for common image containers. Returns ext or None."""
    if data[:3] == b"\xff\xd8\xff":
        return ".jpg"
    if data[:8] == b"\x89PNG\r\n\x1a\n":
        return ".png"
    if data[:6] in (b"GIF87a", b"GIF89a"):
        return ".gif"
    if data[:4] == b"RIFF" and data[8:12] == b"WEBP":
        return ".webp"
    return None


class StorageBackend(ABC):
    @abstractmethod
    def save(self, key: str, data: bytes, content_type: str = "application/octet-stream") -> str:
        """Persist bytes under key → return canonical storage_key."""

    @abstractmethod
    def open(self, key: str):
        """Return a binary file-like for a stored key (local) or raise KeyError."""

    @abstractmethod
    def exists(self, key: str) -> bool: ...

    @abstractmethod
    def presigned_url(self, key: str) -> str | None:
        """Short-lived direct URL (S3) or None when streaming must go through the API."""


class LocalStorage(StorageBackend):
    def __init__(self, root: str):
        self.root = Path(root)
        self.root.mkdir(parents=True, exist_ok=True)

    def _path(self, key: str) -> Path:
        if not is_safe_key(key):
            raise KeyError("unsafe storage key")
        return self.root / key

    def save(self, key: str, data: bytes, content_type: str = "application/octet-stream") -> str:
        path = self._path(key)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
        return key

    def open(self, key: str):
        path = self._path(key)
        if not path.is_file():
            raise KeyError(key)
        return path.open("rb")

    def exists(self, key: str) -> bool:
        try:
            return self._path(key).is_file()
        except KeyError:
            return False

    def presigned_url(self, key: str) -> str | None:
        return None


class S3Storage(StorageBackend):
    """S3-compatible backend (AWS S3 or MinIO). One client per process."""

    def __init__(self):
        import boto3
        s = get_settings()
        if not s.S3_ENDPOINT or not s.S3_ACCESS_KEY:
            raise RuntimeError("S3 storage selected but S3_ENDPOINT/S3_ACCESS_KEY unset")
        self.bucket = s.S3_BUCKET
        self.expiry = s.S3_PRESIGN_EXPIRY_S
        self.client = boto3.client(
            "s3", endpoint_url=s.S3_ENDPOINT, region_name=s.S3_REGION,
            aws_access_key_id=s.S3_ACCESS_KEY, aws_secret_access_key=s.S3_SECRET_KEY,
            use_ssl=s.S3_USE_SSL)

    def save(self, key: str, data: bytes, content_type: str = "application/octet-stream") -> str:
        if not is_safe_key(key):
            raise KeyError("unsafe storage key")
        self.client.put_object(Bucket=self.bucket, Key=key, Body=data, ContentType=content_type)
        return f"s3://{self.bucket}/{key}"

    @staticmethod
    def split(storage_key: str) -> tuple[str, str]:
        assert storage_key.startswith("s3://")
        rest = storage_key[5:]
        bucket, _, key = rest.partition("/")
        return bucket, key

    def open(self, key: str):
        raise KeyError("stream S3 objects via presigned_url, not open()")

    def exists(self, key: str) -> bool:
        try:
            self.client.head_object(Bucket=self.bucket, Key=key)
            return True
        except Exception:  # noqa: BLE001 — existence probe must answer bool, never raise
            return False

    def presigned_url(self, key: str) -> str | None:
        if not is_safe_key(key):
            return None
        try:
            return self.client.generate_presigned_url(
                "get_object", Params={"Bucket": self.bucket, "Key": key}, ExpiresIn=self.expiry)
        except Exception as exc:  # noqa: BLE001 — presign failure degrades to API streaming/404
            log.warning("presign-failed err=%s", type(exc).__name__)
            return None


def _provider_name() -> str:
    if "STORAGE_PROVIDER" in os.environ:
        return (os.environ["STORAGE_PROVIDER"] or "").strip().lower() or "local"
    legacy = (os.environ.get("STORAGE_BACKEND") or "").strip().lower()
    if legacy:
        return legacy
    return get_settings().STORAGE_PROVIDER.lower()


_backend: StorageBackend | None = None


def get_backend() -> StorageBackend:
    global _backend
    if _backend is None:
        _backend = S3Storage() if _provider_name() == "s3" else LocalStorage(get_settings().STORAGE_DIR)
    return _backend


def reset_backend() -> None:
    """Test hook: drop the cached backend so env changes take effect."""
    global _backend
    _backend = None


# ---------- High-level helpers used by routers/pipeline ----------

def save_upload(filename: str, data: bytes, prefix: str = "videos",
                content_type: str = "application/octet-stream") -> str:
    return get_backend().save(_secure_key(prefix, filename), data, content_type)


def resolve_path(storage_key: str) -> Path | None:
    """Local filesystem path for pipeline processing, or None for S3 objects."""
    if storage_key.startswith("s3://"):
        return None
    backend = get_backend()
    if isinstance(backend, LocalStorage):
        try:
            return backend._path(storage_key)
        except KeyError:
            return None
    return None


def open_stream(storage_key: str):
    """Binary stream for API downloads. Supports local keys and s3:// keys (same bucket)."""
    backend = get_backend()
    if storage_key.startswith("s3://"):
        bucket, key = S3Storage.split(storage_key)
        if isinstance(backend, S3Storage) and bucket == backend.bucket and backend.exists(key):
            import io
            buf = io.BytesIO()
            backend.client.download_fileobj(bucket, key, buf)
            buf.seek(0)
            return buf
        raise KeyError(storage_key)
    return backend.open(storage_key)


def download_url(storage_key: str) -> str | None:
    """Presigned URL when the backend supports it, else None (stream via API)."""
    backend = get_backend()
    key = S3Storage.split(storage_key)[1] if storage_key.startswith("s3://") else storage_key
    return backend.presigned_url(key)
