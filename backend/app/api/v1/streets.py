"""Streets + video upload/list. Admin + officer can read; uploads are admin-only."""
from pathlib import Path

from fastapi import APIRouter, Depends, HTTPException, Query, Request, UploadFile
from sqlalchemy import func
from sqlalchemy.orm import Session

from app.core.deps import audit, get_db, page_params, require_role
from app.core.rate_limit import limiter
from app.models.analysis import Analysis
from app.models.geo import Street, Video
from app.models.user import User
from app.schemas import StreetOut, VideoOut
from app.services.storage import resolve_path, save_upload
from app.services.video_pipeline import ALLOWED_EXTS, validate_video

router = APIRouter(tags=["streets"])


def _enrich_batch(db: Session, streets: list[Street]) -> list[dict]:
    """Two aggregate queries total — no per-street N+1, regardless of page size."""
    ids = [s.id for s in streets]
    if not ids:
        return []
    counts = dict(db.query(Video.street_id, func.count(Video.id))
                  .filter(Video.street_id.in_(ids)).group_by(Video.street_id).all())
    latest_by_street: dict[int, Analysis] = {}
    for a in (db.query(Analysis)
              .filter(Analysis.street_id.in_(ids), Analysis.status == "done")
              .order_by(Analysis.street_id, Analysis.created_at.desc()).all()):
        latest_by_street.setdefault(a.street_id, a)
    out = []
    for s in streets:
        latest = latest_by_street.get(s.id)
        out.append({"id": s.id, "name": s.name, "area": s.area, "latitude": s.latitude,
                    "longitude": s.longitude, "video_count": counts.get(s.id, 0),
                    "latest_severity": latest.overall_severity if latest else None,
                    "latest_analysis_at": latest.created_at if latest else None})
    return out


def _enrich(db: Session, s: Street) -> dict:
    return _enrich_batch(db, [s])[0]


@router.get("/streets", response_model=list[StreetOut])
def list_streets(limit: int = Query(50, ge=1, le=10000), offset: int = Query(0, ge=0),
                 db: Session = Depends(get_db), user: User = Depends(require_role("admin", "officer"))):
    lim, off = page_params(limit, offset)
    streets = db.query(Street).order_by(Street.name).limit(lim).offset(off).all()
    return _enrich_batch(db, streets)


@router.get("/streets/{street_id}", response_model=StreetOut)
def get_street(street_id: int, db: Session = Depends(get_db),
               user: User = Depends(require_role("admin", "officer"))):
    s = db.query(Street).filter(Street.id == street_id).first()
    if not s:
        raise HTTPException(404, "Street not found")
    return _enrich(db, s)


@router.get("/videos", response_model=list[VideoOut])
def list_videos(street_id: int | None = None, limit: int = Query(50, ge=1, le=10000),
                offset: int = Query(0, ge=0), db: Session = Depends(get_db),
                user: User = Depends(require_role("admin", "officer"))):
    q = db.query(Video).order_by(Video.created_at.desc())
    if street_id:
        q = q.filter(Video.street_id == street_id)
    lim, off = page_params(limit, offset)
    return q.limit(lim).offset(off).all()


@router.post("/videos/upload", response_model=VideoOut, status_code=201)
@limiter.limit("10/minute")
def upload_video(request: Request, street_id: int, file: UploadFile,
                 db: Session = Depends(get_db), user: User = Depends(require_role("admin"))):
    street = db.query(Street).filter(Street.id == street_id).first()
    if not street:
        raise HTTPException(404, "Street not found")
    ext = Path(file.filename or "").suffix.lower()
    if ext not in ALLOWED_EXTS:
        raise HTTPException(422, f"Unsupported file type {ext}")
    data = file.file.read()
    key = save_upload(file.filename or "upload.mp4", data,
                      content_type=file.content_type or "video/mp4")
    v = Video(street_id=street_id, storage_key=key, filename=file.filename or "upload",
              size_bytes=len(data), status="ready")
    db.add(v)
    db.flush()
    path = resolve_path(key)
    if path and path.exists():
        ok, msg, dur = validate_video(path, len(data))
        v.status = "ready" if ok else "invalid"
        v.duration_s = dur
        if not ok:
            db.commit()
            raise HTTPException(422, f"Video validation failed: {msg}")
    audit(db, actor_id=user.id, action="video.upload", entity="video",
          entity_id=str(v.id), meta={"street_id": street_id})
    db.commit()
    db.refresh(v)
    return v
