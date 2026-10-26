"""Test-suite defaults: rate limiting OFF (all tests share one client IP, so
per-minute buckets would otherwise leak across tests). Rate limiting itself
is proven by test_rate_limit_enforced in test_prod.py with the limiter on."""
from app.core.rate_limit import limiter

limiter.enabled = False
