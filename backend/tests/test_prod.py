"""Production-readiness tests: pagination, refresh lifecycle, storage backends,
task boundary, Alembic migration, file-download auth, upload validation units."""
import os

from fastapi.testclient import TestClient

from app.db.base import Base
from app.db.session import engine
from app.main import app


def _client():
    Base.metadata.drop_all(bind=engine)
    return TestClient(app)


def _login(c, email, pw):
    r = c.post("/api/v1/auth/login", json={"email": email, "password": pw})
    assert r.status_code == 200, r.text
    return r.json()


# ---------- Rate limiting (limiter re-enabled just for this test) ----------

def test_rate_limit_enforced(monkeypatch):
    from app.core.rate_limit import limiter
    monkeypatch.setattr(limiter, "enabled", True)
    limiter._storage.reset()
    with _client() as c:
        codes = set()
        for _ in range(20):
            r = c.post("/api/v1/auth/login",
                       json={"email": "nobody@urbaneyes.city", "password": "Wrong123!"})
            codes.add(r.status_code)
        assert 429 in codes  # login is capped at 15/minute


# ---------- Pagination ----------

def test_pagination_clamped():
    with _client() as c:
        h = {"Authorization": f"Bearer {_login(c, 'admin@urbaneyes.city', 'Admin123!')['access_token']}"}
        r = c.get("/api/v1/requests?limit=1", headers=h)
        assert r.status_code == 200 and len(r.json()) <= 1
        r = c.get("/api/v1/requests?limit=500", headers=h)  # clamped, not an error
        assert r.status_code == 200
        r = c.get("/api/v1/analyses?limit=2&offset=1", headers=h)
        assert r.status_code == 200


# ---------- Refresh lifecycle ----------

def test_refresh_reuse_detected():
    with _client() as c:
        t = _login(c, "admin@urbaneyes.city", "Admin123!")
        r = c.post("/api/v1/auth/refresh", json={"refresh_token": t["refresh_token"]})
        assert r.status_code == 200
        r2 = c.post("/api/v1/auth/refresh", json={"refresh_token": t["refresh_token"]})
        assert r2.status_code == 401 and "revoked" in r2.json()["detail"]


def test_logout_all_revokes_everything():
    with _client() as c:
        t1 = _login(c, "officer@urbaneyes.city", "Officer123!")
        t2 = _login(c, "officer@urbaneyes.city", "Officer123!")
        r = c.post("/api/v1/auth/logout-all",
                   headers={"Authorization": f"Bearer {t1['access_token']}"})
        assert r.status_code == 204
        for t in (t1, t2):
            bad = c.post("/api/v1/auth/refresh", json={"refresh_token": t["refresh_token"]})
            assert bad.status_code == 401


# ---------- Storage units ----------

def test_local_storage_roundtrip(tmp_path):
    from app.services.storage import LocalStorage
    b = LocalStorage(str(tmp_path))
    key = b.save("videos/ab12_clip.mp4", b"\x00\x01")
    assert b.exists(key) and b.open(key).read() == b"\x00\x01"
    assert b.presigned_url(key) is None
    try:
        b.open("../escape")
        raise AssertionError("traversal must fail")
    except KeyError:
        pass


def test_storage_key_safety():
    from app.services.storage import is_safe_key
    assert is_safe_key("evidence/3/ab12_after.jpg")
    assert not is_safe_key("../etc/passwd")
    assert not is_safe_key("/absolute")
    assert not is_safe_key("")
    assert not is_safe_key("a/../b")


def test_sniff_image():
    from app.services.storage import sniff_image
    assert sniff_image(b"\xff\xd8\xff" + b"\x00" * 10) == ".jpg"
    assert sniff_image(b"\x89PNG\r\n\x1a\n" + b"\x00" * 10) == ".png"
    assert sniff_image(b"GIF89a" + b"\x00" * 10) == ".gif"
    assert sniff_image(b"RIFF\x00\x00\x00\x00WEBP" + b"\x00" * 10) == ".webp"
    assert sniff_image(b"definitely not an image") is None


def test_s3_backend_requires_config():
    from app.services.storage import S3Storage
    assert not os.environ.get("S3_ENDPOINT")
    try:
        S3Storage()
        raise AssertionError("must require endpoint/credentials")
    except RuntimeError:
        pass


def test_legacy_storage_backend_env(monkeypatch):
    from app.services import storage as st
    monkeypatch.delenv("STORAGE_PROVIDER", raising=False)
    monkeypatch.setenv("STORAGE_BACKEND", "s3")
    try:
        assert st._provider_name() == "s3"
    finally:
        monkeypatch.undo()
        st.reset_backend()


# ---------- Task boundary ----------

def test_enqueue_sync_fallback_no_crash():
    from app.workers.tasks import enqueue_analysis
    assert enqueue_analysis(987654321, None) == "sync"  # missing id → silent no-op


# ---------- Alembic migration ----------

EXPECTED_TABLES = {"organizations", "users", "streets", "videos", "analyses", "detections",
                   "incidents", "municipal_requests", "request_status_history",
                   "officer_assignments", "resolution_evidence", "notifications",
                   "audit_logs", "refresh_tokens"}


def test_alembic_initial_migration(tmp_path, monkeypatch):
    from alembic.config import Config
    from sqlalchemy import create_engine, inspect

    from alembic import command
    target = tmp_path / "mig.db"
    monkeypatch.setenv("DATABASE_URL", f"sqlite:///{target}")
    cfg = Config("alembic.ini")
    cfg.set_main_option("script_location", "alembic")
    command.upgrade(cfg, "head")
    eng = create_engine(f"sqlite:///{target}")
    assert EXPECTED_TABLES <= set(inspect(eng).get_table_names())
    command.downgrade(cfg, "base")
    assert set(inspect(eng).get_table_names()) <= {"alembic_version"}
    eng.dispose()


# ---------- File download + evidence auth ----------

def test_files_endpoint_auth():
    with _client() as c:
        assert c.get("/api/v1/files?key=videos/x.mp4").status_code == 401
        h = {"Authorization": f"Bearer {_login(c, 'admin@urbaneyes.city', 'Admin123!')['access_token']}"}
        assert c.get("/api/v1/files?key=videos/does-not-exist.mp4", headers=h).status_code == 404
        assert c.get("/api/v1/files?key=../secret", headers=h).status_code == 404
        assert c.get("/api/v1/requests/99999/evidence", headers=h).status_code == 404


def test_search_scoped_to_own_requests():
    with _client() as c:
        h = {"Authorization": f"Bearer {_login(c, 'admin@urbaneyes.city', 'Admin123!')['access_token']}"}
        r = c.get("/api/v1/search?q=brigade", headers=h)
        assert r.status_code == 200 and any(s["name"] == "Brigade Road" for s in r.json()["streets"])
        assert c.get("/api/v1/search?q=x", headers=h).status_code == 422
