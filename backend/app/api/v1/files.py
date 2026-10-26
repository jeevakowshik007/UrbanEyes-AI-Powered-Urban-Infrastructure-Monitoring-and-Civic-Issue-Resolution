"""Authenticated file downloads.

Clients never touch storage directly: local files stream through this endpoint
(with visibility checks), S3 objects redirect to short-lived presigned URLs.
Only keys referenced by the database are servable — no arbitrary path access.
"""
import mimetypes

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import FileResponse
from sqlalchemy import or_
from sqlalchemy.orm import Session

from app.core.deps import get_db, require_role
from app.models.geo import Video
from app.models.request import MunicipalRequest, ResolutionEvidence
from app.models.user import User
from app.services.storage import download_url, is_safe_key, resolve_path

router = APIRouter(tags=["files"])


def _can_view_request(user: User, req: MunicipalRequest) -> bool:
    return user.role == "officer" or req.submitted_by == user.id


@router.get("/files")
def download(key: str, db: Session = Depends(get_db),
             user: User = Depends(require_role("admin", "officer"))):
    if not is_safe_key(key):
        raise HTTPException(404, "File not found")
    storage_key: str | None = None
    if key.startswith("videos/"):
        row = db.query(Video).filter(or_(Video.storage_key == key,
                                         Video.storage_key.like(f"%/{key}"))).first()
        if row:
            storage_key = row.storage_key
    elif key.startswith("evidence/"):
        row = db.query(ResolutionEvidence).filter(
            or_(ResolutionEvidence.storage_key == key,
                ResolutionEvidence.storage_key.like(f"%/{key}"))).first()
        if row:
            req = db.query(MunicipalRequest).filter(
                MunicipalRequest.id == row.request_id).first()
            if req and _can_view_request(user, req):
                storage_key = row.storage_key
    if storage_key is None:
        raise HTTPException(404, "File not found")  # 404 (not 403) to avoid leaking existence
    if storage_key.startswith("s3://"):
        url = download_url(storage_key)
        if not url:
            raise HTTPException(404, "File not found")
        return {"url": url}  # JSON (not redirect): keeps Authorization header off the presigned GET
    path = resolve_path(storage_key)
    if path is None or not path.is_file():
        raise HTTPException(404, "File not found")
    media, _ = mimetypes.guess_type(path.name)
    return FileResponse(path, media_type=media or "application/octet-stream",
                        filename=path.name)
