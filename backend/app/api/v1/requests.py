"""Municipal requests: admin creates (explicit confirm), officer drives lifecycle + evidence."""
from fastapi import APIRouter, Depends, HTTPException, Query, UploadFile
from sqlalchemy.orm import Session

from app.core.config import get_settings
from app.core.deps import audit, get_db, page_params, require_role
from app.models.request import MunicipalRequest, RequestStatusHistory, ResolutionEvidence
from app.models.user import User
from app.schemas import AssignIn, EvidenceOut, HistoryOut, RequestCreate, RequestOut, StatusPatch
from app.services import requests as svc
from app.services.storage import save_upload, sniff_image

router = APIRouter(tags=["requests"])


def _visible_request(db: Session, user: User, req_id: int) -> MunicipalRequest:
    r = db.query(MunicipalRequest).filter(MunicipalRequest.id == req_id).first()
    if not r:
        raise HTTPException(404, "Request not found")
    if user.role == "admin" and r.submitted_by != user.id:
        raise HTTPException(403, "Not your request")
    return r


@router.post("/requests", response_model=RequestOut, status_code=201)
def create_request(body: RequestCreate, db: Session = Depends(get_db),
                   user: User = Depends(require_role("admin"))):
    return svc.create_request(db, admin=user, analysis_id=body.analysis_id, note=body.note)


@router.get("/requests", response_model=list[RequestOut])
def list_requests(status: str | None = None, mine: bool = False,
                  limit: int = Query(50, ge=1, le=10000), offset: int = Query(0, ge=0),
                  db: Session = Depends(get_db),
                  user: User = Depends(require_role("admin", "officer"))):
    q = db.query(MunicipalRequest).order_by(MunicipalRequest.created_at.desc())
    if user.role == "admin":
        q = q.filter(MunicipalRequest.submitted_by == user.id)
    elif mine:
        q = q.filter(MunicipalRequest.assigned_to == user.id)
    if status:
        q = q.filter(MunicipalRequest.status == status)
    lim, off = page_params(limit, offset)
    return q.limit(lim).offset(off).all()


@router.get("/requests/{req_id}", response_model=RequestOut)
def get_request(req_id: int, db: Session = Depends(get_db),
                user: User = Depends(require_role("admin", "officer"))):
    return _visible_request(db, user, req_id)


@router.patch("/requests/{req_id}/status", response_model=RequestOut)
def patch_status(req_id: int, body: StatusPatch, db: Session = Depends(get_db),
                 user: User = Depends(require_role("officer"))):
    r = db.query(MunicipalRequest).filter(MunicipalRequest.id == req_id).first()
    if not r:
        raise HTTPException(404, "Request not found")
    return svc.transition(db, officer=user, req=r, to_status=body.to_status, reason=body.reason)


@router.post("/requests/{req_id}/assignments", response_model=RequestOut)
def assign_request(req_id: int, body: AssignIn, db: Session = Depends(get_db),
                   user: User = Depends(require_role("officer"))):
    r = db.query(MunicipalRequest).filter(MunicipalRequest.id == req_id).first()
    if not r:
        raise HTTPException(404, "Request not found")
    return svc.assign(db, actor=user, req=r, officer_id=body.officer_id)


@router.post("/requests/{req_id}/evidence", response_model=EvidenceOut, status_code=201)
def upload_evidence(req_id: int, kind: str, file: UploadFile, notes: str | None = None,
                    db: Session = Depends(get_db), user: User = Depends(require_role("officer"))):
    if kind not in ("before", "after", "repair"):
        raise HTTPException(422, "kind must be before|after|repair")
    r = db.query(MunicipalRequest).filter(MunicipalRequest.id == req_id).first()
    if not r:
        raise HTTPException(404, "Request not found")
    data = file.file.read()
    cap_mb = get_settings().EVIDENCE_MAX_MB
    if len(data) > cap_mb * 1024 * 1024:
        raise HTTPException(422, f"Evidence image exceeds {cap_mb} MB")
    ext = sniff_image(data)
    if ext is None:
        raise HTTPException(422, "Evidence must be a real JPEG, PNG, GIF or WebP image")
    content_type = {"jpg": "image/jpeg", ".jpg": "image/jpeg", ".png": "image/png",
                    ".gif": "image/gif", ".webp": "image/webp"}.get(ext, "image/jpeg")
    key = save_upload(file.filename or "evidence.jpg", data, prefix=f"evidence/{req_id}",
                      content_type=content_type)
    ev = ResolutionEvidence(request_id=req_id, officer_id=user.id, kind=kind,
                            storage_key=key, notes=notes)
    db.add(ev)
    audit(db, actor_id=user.id, action="evidence.upload", entity="municipal_request",
          entity_id=r.code, meta={"kind": kind})
    db.commit()
    db.refresh(ev)
    return ev


@router.get("/requests/{req_id}/history", response_model=list[HistoryOut])
def get_history(req_id: int, db: Session = Depends(get_db),
                user: User = Depends(require_role("admin", "officer"))):
    _visible_request(db, user, req_id)
    return (db.query(RequestStatusHistory).filter(RequestStatusHistory.request_id == req_id)
            .order_by(RequestStatusHistory.created_at).all())


@router.get("/requests/{req_id}/evidence", response_model=list[EvidenceOut])
def list_evidence(req_id: int, db: Session = Depends(get_db),
                  user: User = Depends(require_role("admin", "officer"))):
    """Resolution evidence for a request — same visibility as the request itself."""
    _visible_request(db, user, req_id)
    return (db.query(ResolutionEvidence).filter(ResolutionEvidence.request_id == req_id)
            .order_by(ResolutionEvidence.created_at).all())
