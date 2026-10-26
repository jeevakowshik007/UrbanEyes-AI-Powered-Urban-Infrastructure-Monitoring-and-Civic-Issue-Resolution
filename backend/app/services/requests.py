"""Municipal request service: creation + auditable state machine + notifications."""
from __future__ import annotations

from datetime import datetime, timezone

from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.core.deps import audit
from app.models.analysis import Analysis, Incident
from app.models.ops import Notification
from app.models.request import TRANSITIONS, MunicipalRequest, OfficerAssignment, RequestStatusHistory
from app.models.user import User


def _code(db: Session) -> str:
    year = datetime.now(timezone.utc).year
    n = db.query(MunicipalRequest).count() + 1
    return f"UE-{year}-{n:04d}"


def create_request(db: Session, *, admin: User, analysis_id: int, note: str | None) -> MunicipalRequest:
    a = db.query(Analysis).filter(Analysis.id == analysis_id).first()
    if not a or a.status != "done":
        raise HTTPException(422, "Analysis not ready — run street analysis first")
    if db.query(MunicipalRequest).filter(MunicipalRequest.analysis_id == analysis_id).first():
        raise HTTPException(409, "A request already exists for this analysis")
    inc = db.query(Incident).filter(Incident.analysis_id == analysis_id).first()
    if not inc:
        inc = Incident(analysis_id=a.id, street_id=a.street_id, severity=a.overall_severity or "weak")
        db.add(inc)
        db.flush()
    req = MunicipalRequest(code=_code(db), incident_id=inc.id, analysis_id=a.id,
                           street_id=a.street_id, submitted_by=admin.id,
                           status="pending", severity=a.overall_severity or "weak", note=note)
    db.add(req)
    db.flush()
    db.add(RequestStatusHistory(request_id=req.id, actor_id=admin.id,
                                from_status=None, to_status="pending", reason=note))
    inc.status = "requested"
    for off in db.query(User).filter(User.role == "officer", User.is_active == True).all():
        db.add(Notification(user_id=off.id, title=f"New request {req.code}",
                            body=f"{a.overall_severity} issue reported — review required.", kind="request"))
    audit(db, actor_id=admin.id, action="request.create", entity="municipal_request",
          entity_id=req.code, meta={"analysis_id": analysis_id})
    db.commit()
    db.refresh(req)
    return req


def transition(db: Session, *, officer: User, req: MunicipalRequest,
               to_status: str, reason: str | None) -> MunicipalRequest:
    allowed = TRANSITIONS.get(req.status, set())
    if to_status not in allowed:
        raise HTTPException(409, f"Illegal transition {req.status} → {to_status}")
    if to_status == "resolved":
        from app.models.request import ResolutionEvidence
        has_evidence = db.query(ResolutionEvidence).filter(
            ResolutionEvidence.request_id == req.id).first()
        if not has_evidence:
            raise HTTPException(422, "Resolution evidence required before marking resolved")
    if to_status == "rejected" and not reason:
        raise HTTPException(422, "Rejection requires a reason")
    frm = req.status
    req.status = to_status
    db.add(RequestStatusHistory(request_id=req.id, actor_id=officer.id,
                                from_status=frm, to_status=to_status, reason=reason))
    if to_status == "resolved":
        # Close the loop: the underlying incident is verified resolved too.
        inc = db.query(Incident).filter(Incident.id == req.incident_id).first()
        if inc:
            inc.status = "resolved"
    # Notify submitting admin on every transition.
    db.add(Notification(user_id=req.submitted_by, title=f"Request {req.code}: {to_status}",
                        body=reason or f"Status changed {frm} → {to_status}.", kind="status"))
    audit(db, actor_id=officer.id, action="request.transition", entity="municipal_request",
          entity_id=req.code, meta={"from": frm, "to": to_status})
    db.commit()
    db.refresh(req)
    return req


def assign(db: Session, *, actor: User, req: MunicipalRequest, officer_id: int) -> MunicipalRequest:
    officer = db.query(User).filter(User.id == officer_id, User.role == "officer").first()
    if not officer:
        raise HTTPException(404, "Officer not found")
    req.assigned_to = officer.id
    if req.status in ("pending", "under_review", "accepted"):
        frm = req.status
        req.status = "assigned"
        db.add(RequestStatusHistory(request_id=req.id, actor_id=actor.id,
                                    from_status=frm, to_status="assigned",
                                    reason=f"Assigned to {officer.full_name}"))
    db.add(OfficerAssignment(request_id=req.id, officer_id=officer.id, assigned_by=actor.id))
    db.add(Notification(user_id=officer.id, title=f"Assigned {req.code}",
                        body="A municipal request was assigned to you.", kind="assignment"))
    audit(db, actor_id=actor.id, action="request.assign", entity="municipal_request",
          entity_id=req.code, meta={"officer_id": officer_id})
    db.commit()
    db.refresh(req)
    return req
