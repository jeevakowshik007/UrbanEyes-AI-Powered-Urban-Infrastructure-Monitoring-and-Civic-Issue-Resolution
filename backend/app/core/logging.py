"""Structured logging — no secrets, no tracebacks to clients."""
import logging
import sys

_handler = logging.StreamHandler(sys.stdout)
_handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s [%(name)s] %(message)s"))


def get_logger(name: str) -> logging.Logger:
    log = logging.getLogger(f"urbaneyes.{name}")
    if not log.handlers:
        log.addHandler(_handler)
    log.setLevel(logging.INFO)
    return log
