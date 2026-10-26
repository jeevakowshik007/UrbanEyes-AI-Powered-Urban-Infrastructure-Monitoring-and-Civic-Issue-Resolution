"""Analyses + incidents. POST returns 202 (background pipeline); GET polls status."""
from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException, Query, Request
from sqlalchemy.orm import Session

from app.core.deps import audit, get_db, page_params, require_role
from app.core.rate_limit import limiter
from app.models.analysis import Analysis, Incident
from app.models.geo import Street, Video
from app.models.user import User
from app.schemas import AnalysisCreate, AnalysisOut, IncidentOut
from app.workers.tasks import enqueue_analysis

router = APIRouter(tags=["analyses"])


def _out(a: Analysis) -> dict:
    cats = None
    if a.overall_severity:
        cats = {"road_condition": a.cat_road, "waste_management": a.cat_waste,
                "drainage": a.cat_drainage, "street_infrastructure": a.cat_infra}
    return {"id": a.id, "street_id": a.street_id, "video_id": a.video_id, "status": a.status,
            "overall_severity": a.overall_severity, "weak_count": a.weak_count,
            "medium_count": a.medium_count, "critical_count": a.critical_count,
            "categories": cats, "reason": a.reason, "recommendation": a.recommendation,
            "request_recommended": a.request_recommended, "reasoning_source": a.reasoning_source,
            "created_at": a.created_at}


@router.post("/analyses", status_code=202)
@limiter.limit("20/minute")
def start_analysis(body: AnalysisCreate, request: Request, bg: BackgroundTasks,
                   db: Session = Depends(get_db), user: User = Depends(require_role("admin"))):
    street = db.query(Street).filter(Street.id == body.street_id).first()
    if not street:
        raise HTTPException(404, "Street not found")
    video_id = body.video_id
    if video_id is None:
        latest = (db.query(Video).filter(Video.street_id == body.street_id,
                                         Video.status == "ready")
                  .order_by(Video.created_at.desc()).first())
        if not latest:
            raise HTTPException(422, "No recorded video for this street — upload one first")
        video_id = latest.id
    a = Analysis(street_id=body.street_id, video_id=video_id, created_by=user.id, status="queued")
    db.add(a)
    db.commit()
    db.refresh(a)
    audit(db, actor_id=user.id, action="analysis.start", entity="analysis",
          entity_id=str(a.id), meta={"street_id": body.street_id})
    db.commit()
    mode = enqueue_analysis(a.id, bg)
    return {"analysis_id": a.id, "status": "queued", "mode": mode}


@router.get("/analyses", response_model=list[AnalysisOut])
def list_analyses(street_id: int | None = None, limit: int = Query(50, ge=1, le=10000),
                  offset: int = Query(0, ge=0), db: Session = Depends(get_db),
                  user: User = Depends(require_role("admin", "officer"))):
    q = db.query(Analysis).order_by(Analysis.created_at.desc())
    if street_id:
        q = q.filter(Analysis.street_id == street_id)
    lim, off = page_params(limit, offset)
    return [_out(a) for a in q.limit(lim).offset(off).all()]


@router.get("/analyses/{analysis_id}", response_model=AnalysisOut)
def get_analysis(analysis_id: int, db: Session = Depends(get_db),
                 user: User = Depends(require_role("admin", "officer"))):
    a = db.query(Analysis).filter(Analysis.id == analysis_id).first()
    if not a:
        raise HTTPException(404, "Analysis not found")
    return _out(a)


@router.get("/incidents", response_model=list[IncidentOut])
def list_incidents(severity: str | None = None, limit: int = Query(50, ge=1, le=10000),
                   offset: int = Query(0, ge=0), db: Session = Depends(get_db),
                   user: User = Depends(require_role("admin", "officer"))):
    q = db.query(Incident).order_by(Incident.created_at.desc())
    if severity:
        if severity not in ("weak", "medium", "critical"):
            raise HTTPException(422, "Invalid severity")
        q = q.filter(Incident.severity == severity)
    lim, off = page_params(limit, offset)
    return q.limit(lim).offset(off).all()
