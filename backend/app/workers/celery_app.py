"""Celery application. Broker = REDIS_URL (or CELERY_BROKER_URL override).

No broker configured (or TASK_EAGER=true) → tasks run eagerly in-process,
which is the documented lightweight development mode.
"""
import os

from app.core.config import get_settings

try:
    from celery import Celery
except ImportError:  # celery is optional in dev installs
    Celery = None  # type: ignore


def make_celery():
    s = get_settings()
    if Celery is None:
        return None
    broker = s.celery_broker
    if not broker:
        return None
    app = Celery("urbaneyes", broker=broker,
                 backend=s.CELERY_RESULT_BACKEND or broker)
    app.conf.update(
        task_acks_late=True,
        worker_prefetch_multiplier=1,
        task_time_limit=1800,
        task_soft_time_limit=1500,
        task_default_queue="urbaneyes",
    )
    return app


celery_app = make_celery()


def is_eager() -> bool:
    if os.environ.get("TASK_EAGER", "").lower() in ("1", "true", "yes"):
        return True
    return get_settings().task_eager or celery_app is None
