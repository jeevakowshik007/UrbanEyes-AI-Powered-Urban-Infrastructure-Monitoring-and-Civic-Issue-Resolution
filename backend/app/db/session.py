"""Engine/session factory.

SQLite for lightweight local dev; Postgres with pooling in compose/prod.
Sessions never auto-commit; dependency guarantees rollback on errors.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import get_settings
from app.db.base import Base  # noqa: F401  (model registration side-effect)

settings = get_settings()

if settings.is_sqlite:
    engine = create_engine(settings.DATABASE_URL, pool_pre_ping=True,
                           connect_args={"check_same_thread": False})
else:
    engine = create_engine(
        settings.DATABASE_URL,
        pool_pre_ping=True,
        pool_size=settings.DB_POOL_SIZE,
        max_overflow=settings.DB_MAX_OVERFLOW,
        pool_timeout=settings.DB_POOL_TIMEOUT_S,
        pool_recycle=1800,
    )

# expire_on_commit=False: committed objects stay usable when building responses.
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False,
                            expire_on_commit=False)
