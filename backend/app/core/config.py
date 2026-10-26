"""Central application settings. All secrets come from environment — never hard-code."""
from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    APP_NAME: str = "UrbanEyes"
    APP_ENV: str = "dev"
    API_V1_PREFIX: str = "/api/v1"

    DATABASE_URL: str = "sqlite:///./urbaneyes_dev.db"
    # Postgres pool (ignored for SQLite dev mode)
    DB_POOL_SIZE: int = 10
    DB_MAX_OVERFLOW: int = 20
    DB_POOL_TIMEOUT_S: int = 30

    JWT_SECRET: str = "CHANGE_ME_generate_32plus_random_chars"  # noqa: S105 — dev placeholder; prod requires env secret
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_MINUTES: int = 15
    REFRESH_TOKEN_DAYS: int = 7
    # Canonical expiry names (preferred); fall back to the legacy names above.
    ACCESS_TOKEN_EXPIRE_MINUTES: int | None = None
    REFRESH_TOKEN_EXPIRE_DAYS: int | None = None

    CORS_ORIGINS: str = "http://localhost:5173"

    CV_PROVIDER: str = "mock"  # mock | yolo (computer-vision evidence layer)
    REASONING_PROVIDER: str = "local"  # local (Local Urban Infrastructure Reasoning Engine)
    YOLO26_SEG_WEIGHTS: str = "./weights/yolo26-seg.pt"
    YOLO26_CONF: float = 0.35
    YOLO26_DEVICE: str = "cpu"  # cpu | cuda | auto (resolved at adapter init; auto falls back to cpu)
    YOLO26_IMGSZ: int = 640
    YOLO26_IOU: float = 0.7
    YOLO26_MAX_DET: int = 100
    YOLO26_HALF: bool = False  # fp16: only honored on CUDA, ignored on CPU
    FRAME_SAMPLE_COUNT: int = 12
    # NOTE: FRAME_SAMPLE_FPS was removed — sampling is deterministic count-based
    # (evenly spaced frames); see services/video_pipeline.py.

    # Local reasoning thresholds (deterministic factor scoring, see services/reasoning.py)
    REASONING_SCORE_CRITICAL: float = 0.60
    REASONING_SCORE_MEDIUM: float = 0.32
    MEDIUM_REQUEST_MIN_FINDINGS: int = 3

    STORAGE_BACKEND: str = "local"  # legacy alias, honored if STORAGE_PROVIDER unset
    STORAGE_PROVIDER: str = "local"  # local | s3 (AWS S3 or MinIO)
    STORAGE_DIR: str = "./storage"
    S3_ENDPOINT: str = ""
    S3_BUCKET: str = "urbaneyes"
    S3_REGION: str = "us-east-1"
    S3_ACCESS_KEY: str = ""
    S3_SECRET_KEY: str = ""
    S3_USE_SSL: bool = True
    S3_PRESIGN_EXPIRY_S: int = 3600
    EVIDENCE_MAX_MB: int = 25

    # Async tasks: empty REDIS_URL (or TASK_EAGER=true) → in-process dev execution.
    REDIS_URL: str = ""
    CELERY_BROKER_URL: str = ""
    CELERY_RESULT_BACKEND: str = ""
    TASK_EAGER: bool = True

    PAGE_MAX_LIMIT: int = 200

    MAX_UPLOAD_MB: int = 500
    SEED_DEMO: bool = True

    @property
    def cors_origins(self) -> list[str]:
        return [o.strip() for o in self.CORS_ORIGINS.split(",") if o.strip()]

    @property
    def access_token_minutes(self) -> int:
        return self.ACCESS_TOKEN_EXPIRE_MINUTES or self.ACCESS_TOKEN_MINUTES

    @property
    def refresh_token_days(self) -> int:
        return self.REFRESH_TOKEN_EXPIRE_DAYS or self.REFRESH_TOKEN_DAYS

    @property
    def celery_broker(self) -> str:
        return self.CELERY_BROKER_URL or self.REDIS_URL

    @property
    def task_eager(self) -> bool:
        return self.TASK_EAGER or not self.celery_broker
        return [o.strip() for o in self.CORS_ORIGINS.split(",") if o.strip()]

    @property
    def is_sqlite(self) -> bool:
        return self.DATABASE_URL.startswith("sqlite")


@lru_cache
def get_settings() -> Settings:
    return Settings()
