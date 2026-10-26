"""UrbanEyes API — app factory with CORS, rate limiting, safe error envelope, demo seed."""
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded

from app import models  # noqa: F401  (register metadata)
from app.api.v1.router import v1_routers
from app.core.config import get_settings
from app.core.rate_limit import limiter
from app.db.base import Base
from app.db.session import engine

settings = get_settings()


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Dev mode creates tables directly. Production (APP_ENV=prod) relies on
    # Alembic migrations run as a deploy init job — never auto-DDL there.
    if settings.APP_ENV != "prod":
        Base.metadata.create_all(bind=engine)
    if settings.SEED_DEMO:
        from app.db.session import SessionLocal
        from app.services.seed import seed_demo
        db = SessionLocal()
        try:
            seed_demo(db)
        finally:
            db.close()
    yield


def create_app() -> FastAPI:
    app = FastAPI(title="UrbanEyes API", version="1.0.0", lifespan=lifespan)
    app.state.limiter = limiter
    app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.exception_handler(Exception)
    async def safe_errors(request: Request, exc: Exception):
        from fastapi.exceptions import HTTPException as HE
        if isinstance(exc, HE):
            return JSONResponse({"detail": exc.detail, "code": exc.status_code},
                                status_code=exc.status_code)
        return JSONResponse({"detail": "Internal error", "code": 500}, status_code=500)

    @app.get("/health")
    def health():
        from app.services.ai import yolo_status
        return {"status": "ok", "cv_provider": settings.CV_PROVIDER,
                "reasoning_provider": settings.REASONING_PROVIDER,
                "yolo": yolo_status()}

    for r in v1_routers:
        app.include_router(r, prefix="/api/v1")
    return app


app = create_app()
