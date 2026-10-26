"""Shared dependencies: DB session, current user, RBAC guards, audit helper."""
from collections.abc import Generator

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session

from app.core.security import decode_token
from app.db.session import SessionLocal
from app.models.user import User

bearer = HTTPBearer(auto_error=False)


def get_db() -> Generator[Session, None, None]:
    """Request-scoped session with guaranteed rollback on errors."""
    db = SessionLocal()
    try:
        yield db
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()


def page_params(limit: int = 50, offset: int = 0) -> tuple[int, int]:
    """Clamp list pagination. Never load entire datasets unbounded."""
    from app.core.config import get_settings
    cap = get_settings().PAGE_MAX_LIMIT
    return min(max(1, limit), cap), max(0, offset)


def get_current_user(
    creds: HTTPAuthorizationCredentials | None = Depends(bearer),
    db: Session = Depends(get_db),
) -> User:
    if creds is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authenticated")
    try:
        payload = decode_token(creds.credentials)
    except ValueError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or expired token")
    if payload.get("typ") != "access":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token type")
    user = db.query(User).filter(User.email == payload.get("sub")).first()
    if user is None or not user.is_active:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Account unavailable")
    return user


def require_role(*roles: str):
    """RBAC gate: `Depends(require_role('admin'))`. Admins never get officer routes and vice versa."""
    def guard(user: User = Depends(get_current_user)) -> User:
        if user.role not in roles:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Insufficient role")
        return user
    return guard


def audit(db: Session, *, actor_id: int | None, action: str, entity: str, entity_id: str, meta: dict | None = None):
    import json

    from app.models.ops import AuditLog
    db.add(AuditLog(actor_id=actor_id, action=action, entity=entity,
                    entity_id=str(entity_id), meta_json=json.dumps(meta or {})))
