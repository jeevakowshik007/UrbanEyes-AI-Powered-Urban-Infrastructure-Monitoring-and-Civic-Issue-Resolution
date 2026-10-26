"""Rate limiting via slowapi. Counts per client IP; auth/upload/analysis are strictest."""
from slowapi import Limiter
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address, default_limits=["100/minute"])
