"""Auth: register / login / refresh / logout / me. Rate-limited, audited."""
from datetime import datetime, timedelta, timezone

from fastapi import APIRouter, Depends, HTTPException, Request, status
from sqlalchemy.orm import Session

from app.core.deps import audit, get_current_user, get_db
from app.core.rate_limit import limiter
from app.core.security import create_access_token, create_refresh_token, decode_token, hash_password, verify_password
from app.models.ops import RefreshToken
from app.models.user import User
from app.schemas import LoginIn, RegisterIn, TokenOut, UserOut

router = APIRouter(prefix="/auth", tags=["auth"])


def _naive(dt: datetime | None) -> datetime | None:
    """SQLite returns naive datetimes, Postgres aware ones — normalize for comparison."""
    return dt.replace(tzinfo=None) if dt is not None and dt.tzinfo is not None else dt


def _utcnow_naive() -> datetime:
    """Naive UTC now — matches SQLite-stored datetimes (Postgres returns aware;
    use auth._naive() when comparing values read back from the DB)."""
    return datetime.now(timezone.utc).replace(tzinfo=None)


def _purge_expired(db: Session, user_id: int) -> None:
    """Housekeeping: drop tokens that are expired or long-revoked (keeps table small)."""
    now = _utcnow_naive()
    old = now - timedelta(days=30)
    db.query(RefreshToken).filter(
        RefreshToken.user_id == user_id,
        (RefreshToken.expires_at < now) | (RefreshToken.revoked == True)).filter(
        RefreshToken.created_at < old).delete(synchronize_session=False)


def _tokens(db: Session, user: User) -> TokenOut:
    refresh = create_refresh_token(user.email)
    payload = decode_token(refresh)
    db.add(RefreshToken(user_id=user.id, jti=payload["jti"],
                        expires_at=datetime.fromtimestamp(payload["exp"], tz=timezone.utc)))
    db.commit()
    return TokenOut(access_token=create_access_token(user.email, user.role), refresh_token=refresh)


@router.post("/register", response_model=TokenOut, status_code=201)
@limiter.limit("10/minute")
def register(body: RegisterIn, request: Request, db: Session = Depends(get_db)):
    if body.role not in ("admin", "officer"):
        raise HTTPException(422, "role must be admin or officer")
    if db.query(User).filter(User.email == body.email).first():
        raise HTTPException(409, "Email already registered")
    user = User(email=body.email, password_hash=hash_password(body.password),
                full_name=body.full_name, role=body.role)
    db.add(user)
    db.commit()
    db.refresh(user)
    audit(db, actor_id=user.id, action="auth.register", entity="user", entity_id=str(user.id))
    db.commit()
    return _tokens(db, user)


@router.post("/login", response_model=TokenOut)
@limiter.limit("15/minute")
def login(body: LoginIn, request: Request, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == body.email).first()
    if not user or not verify_password(body.password, user.password_hash):
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Invalid credentials")
    if not user.is_active:
        raise HTTPException(403, "Account disabled")
    _purge_expired(db, user.id)
    db.commit()
    return _tokens(db, user)


@router.post("/refresh", response_model=TokenOut)
def refresh(body: dict, db: Session = Depends(get_db)):
    try:
        payload = decode_token(body.get("refresh_token", ""))
    except ValueError:
        raise HTTPException(401, "Refresh token invalid or expired — please sign in again")
    if payload.get("typ") != "refresh":
        raise HTTPException(401, "Invalid refresh token")
    rec = db.query(RefreshToken).filter(RefreshToken.jti == payload.get("jti")).first()
    if not rec or rec.revoked:
        raise HTTPException(401, "Refresh token revoked — please sign in again")
    if _naive(rec.expires_at) < _utcnow_naive():  # type: ignore[operator]
        raise HTTPException(401, "Refresh token expired — please sign in again")
    rec.revoked = True  # rotation: single-use refresh tokens
    user = db.query(User).filter(User.email == payload.get("sub")).first()
    if not user or not user.is_active:
        raise HTTPException(401, "Account unavailable")
    _purge_expired(db, user.id)
    db.commit()
    return _tokens(db, user)


@router.post("/logout", status_code=204)
def logout(body: dict, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    try:
        jti = decode_token(body.get("refresh_token", "")).get("jti")
        rec = db.query(RefreshToken).filter(RefreshToken.jti == jti).first()
        if rec:
            rec.revoked = True
            db.commit()
    except ValueError:
        pass


@router.post("/logout-all", status_code=204)
def logout_all(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    """Revoke every refresh token for this user (lost/stolen device)."""
    db.query(RefreshToken).filter(RefreshToken.user_id == user.id,
                                  RefreshToken.revoked == False).update(
        {"revoked": True}, synchronize_session=False)
    audit(db, actor_id=user.id, action="auth.logout_all", entity="user", entity_id=str(user.id))
    db.commit()


@router.get("/me", response_model=UserOut)
def me(user: User = Depends(get_current_user)):
    return user
