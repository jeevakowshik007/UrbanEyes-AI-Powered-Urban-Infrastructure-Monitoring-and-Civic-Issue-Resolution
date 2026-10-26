"""Notifications, global search, profile/settings basics."""
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import or_
from sqlalchemy.orm import Session

from app.core.deps import get_db, page_params, require_role
from app.models.analysis import Analysis
from app.models.geo import Street
from app.models.ops import Notification
from app.models.request import MunicipalRequest
from app.models.user import User
from app.schemas import DashboardOut, NotificationOut, SearchOut

router = APIRouter(tags=["ops"])


@router.get("/notifications", response_model=list[NotificationOut])
def list_notifications(unread_only: bool = False, limit: int = Query(50, ge=1, le=10000),
                       offset: int = Query(0, ge=0), db: Session = Depends(get_db),
                       user: User = Depends(require_role("admin", "officer"))):
    q = db.query(Notification).filter(Notification.user_id == user.id).order_by(Notification.created_at.desc())
    if unread_only:
        q = q.filter(Notification.is_read == False)
    lim, off = page_params(limit, offset)
    return q.limit(lim).offset(off).all()


@router.patch("/notifications/{nid}/read", response_model=NotificationOut)
def mark_read(nid: int, db: Session = Depends(get_db),
              user: User = Depends(require_role("admin", "officer"))):
    n = db.query(Notification).filter(Notification.id == nid, Notification.user_id == user.id).first()
    if not n:
        raise HTTPException(404, "Notification not found")
    n.is_read = True
    db.commit()
    db.refresh(n)
    return n


@router.get("/search", response_model=SearchOut)
def search(q: str, db: Session = Depends(get_db),
           user: User = Depends(require_role("admin", "officer"))):
    if len(q.strip()) < 2:
        raise HTTPException(422, "Query too short")
    like = f"%{q.strip()}%"
    streets = db.query(Street).filter(or_(Street.name.ilike(like), Street.area.ilike(like))).limit(10).all()
    reqs = db.query(MunicipalRequest).filter(MunicipalRequest.code.ilike(like)).limit(10).all()
    if user.role == "admin":
        reqs = [r for r in reqs if r.submitted_by == user.id]
    return {"streets": [{"id": s.id, "name": s.name, "area": s.area} for s in streets],
            "requests": [{"id": r.id, "code": r.code, "status": r.status} for r in reqs]}


@router.get("/dashboard", response_model=DashboardOut)
def dashboard(db: Session = Depends(get_db), user: User = Depends(require_role("admin", "officer"))):
    """Real aggregates — never fake. Answers: what's critical, what's moving, what's stuck."""
    crit = db.query(Analysis).filter(Analysis.status == "done", Analysis.overall_severity == "critical").count()
    total_analyses = db.query(Analysis).count()
    open_reqs = db.query(MunicipalRequest).filter(
        MunicipalRequest.status.notin_(["resolved", "rejected"])).count()
    by_status: dict[str, int] = {}
    for st in ("pending", "under_review", "accepted", "assigned", "in_progress", "resolved", "rejected"):
        by_status[st] = db.query(MunicipalRequest).filter(MunicipalRequest.status == st).count()
    recent = (db.query(Analysis).order_by(Analysis.created_at.desc()).limit(5).all())
    return {"critical_analyses": crit, "total_analyses": total_analyses,
            "open_requests": open_reqs, "requests_by_status": by_status,
            "recent_analysis_ids": [a.id for a in recent]}
