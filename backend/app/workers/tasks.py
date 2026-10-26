"""Task boundary for analysis work.

ONE implementation of the pipeline lives in services/pipeline.py.
These tasks only manage execution context (own DB session) and routing
(Celery worker vs eager in-process) — no duplicated pipeline logic.
"""
from __future__ import annotations

from fastapi import BackgroundTasks

from app.core.logging import get_logger
from app.db.session import SessionLocal
from app.services.pipeline import run_analysis

log = get_logger("tasks")

try:
    from app.workers.celery_app import celery_app, is_eager
except ImportError:  # pragma: no cover
    celery_app = None

    def is_eager() -> bool:
        return True


def _execute(analysis_id: int) -> None:
    """Run the pipeline with a dedicated session. Single entry point for all modes."""
    db = SessionLocal()
    try:
        run_analysis(db, analysis_id)
    finally:
        db.close()


def _celery_run(self, analysis_id: int) -> None:
    _execute(analysis_id)


if celery_app is not None:
    _celery_run = celery_app.task(name="urbaneyes.run_analysis", bind=True,
                                  max_retries=2, autoretry_for=(Exception,),
                                  retry_backoff=30)(_celery_run)


def enqueue_analysis(analysis_id: int, bg: BackgroundTasks | None = None) -> str:
    """Route analysis work: Celery worker when a broker is configured,
    otherwise FastAPI BackgroundTasks (dev). Returns the mode used."""
    if not is_eager() and celery_app is not None and _celery_run is not None:
        _celery_run.delay(analysis_id)
        log.info("enqueued analysis=%d via celery", analysis_id)
        return "celery"
    if bg is None:
        _execute(analysis_id)  # synchronous fallback (tests, scripts)
        return "sync"
    bg.add_task(_execute, analysis_id)
    return "background"
