"""Data-integrity tests: FK linkage, history/audit/notifications, severity
consistency, timestamps, no orphans, no impossible states — after a full flow."""
import time

from fastapi.testclient import TestClient

from app.db.base import Base
from app.db.session import SessionLocal, engine
from app.main import app
from app.models.analysis import Analysis, Detection, Incident
from app.models.geo import Video
from app.models.ops import AuditLog, Notification
from app.models.request import MunicipalRequest, RequestStatusHistory


def _login(c, email, pw):
    r = c.post("/api/v1/auth/login", json={"email": email, "password": pw})
    assert r.status_code == 200, r.text
    return r.json()


def _run_full_flow(c, ah, oh):
    """Admin analyzes street 2 end-to-end through officer resolve. Returns request id."""
    import os
    import tempfile

    import cv2
    import numpy as np
    fd, tmp = tempfile.mkstemp(suffix=".mp4")
    os.close(fd)
    w = cv2.VideoWriter(tmp, cv2.VideoWriter_fourcc(*"mp4v"), 5, (64, 64))
    for i in range(10):
        w.write(np.full((64, 64, 3), i * 20, dtype=np.uint8))
    w.release()
    with open(tmp, "rb") as f:
        assert c.post("/api/v1/videos/upload", params={"street_id": 2},
                      files={"file": ("s.mp4", f, "video/mp4")}, headers=ah).status_code == 201
    os.remove(tmp)
    aid = c.post("/api/v1/analyses", json={"street_id": 2}, headers=ah).json()["analysis_id"]
    for _ in range(60):
        a = c.get(f"/api/v1/analyses/{aid}", headers=ah).json()
        if a["status"] in ("done", "failed"):
            break
        time.sleep(0.5)
    assert a["status"] == "done", a
    req = c.post("/api/v1/requests", json={"analysis_id": aid}, headers=ah).json()
    rid = req["id"]
    me_officer = c.get("/api/v1/auth/me", headers=oh).json()
    for st in ("under_review", "accepted"):
        assert c.patch(f"/api/v1/requests/{rid}/status",
                       json={"to_status": st}, headers=oh).status_code == 200
    assert c.post(f"/api/v1/requests/{rid}/assignments",
                  json={"officer_id": me_officer["id"]}, headers=oh).status_code == 200
    assert c.patch(f"/api/v1/requests/{rid}/status",
                   json={"to_status": "in_progress"}, headers=oh).status_code == 200
    assert c.post(f"/api/v1/requests/{rid}/evidence?kind=after",
                  files={"file": ("a.jpg", b"\xff\xd8\xff\xe0" + b"\x00" * 32,
                                   "image/jpeg")}, headers=oh).status_code == 201
    assert c.patch(f"/api/v1/requests/{rid}/status",
                   json={"to_status": "resolved"}, headers=oh).status_code == 200
    return rid, aid


def test_full_flow_data_integrity(monkeypatch):
    from app.core.config import get_settings
    monkeypatch.setattr(get_settings(), "CV_PROVIDER", "mock")
    Base.metadata.drop_all(bind=engine)
    with TestClient(app) as c:
        ah = {"Authorization": f"Bearer {_login(c, 'admin@urbaneyes.city', 'Admin123!')['access_token']}"}
        oh = {"Authorization": f"Bearer {_login(c, 'officer@urbaneyes.city', 'Officer123!')['access_token']}"}
        admin = c.get("/api/v1/auth/me", headers=ah).json()
        officer = c.get("/api/v1/auth/me", headers=oh).json()
        rid, aid = _run_full_flow(c, ah, oh)

        db = SessionLocal()
        try:
            req = db.query(MunicipalRequest).filter_by(id=rid).one()
            analysis = db.query(Analysis).filter_by(id=aid).one()
            incident = db.query(Incident).filter_by(analysis_id=aid).one()
            # Chain linkage
            assert req.analysis_id == analysis.id == incident.analysis_id
            assert req.incident_id == incident.id
            assert req.street_id == analysis.street_id == incident.street_id
            # Severity consistency + only legal values
            assert req.severity == analysis.overall_severity == incident.severity
            assert req.severity in ("weak", "medium", "critical")
            assert req.status == "resolved" and incident.status == "resolved"
            # Parties + assignment
            assert req.submitted_by == admin["id"] and req.assigned_to == officer["id"]
            # Video + detections linked, timestamps set
            assert db.query(Video).filter_by(id=analysis.video_id).one().street_id == analysis.street_id
            assert db.query(Detection).filter_by(analysis_id=aid).count() >= 1
            for obj in (req, analysis, incident):
                assert obj.created_at is not None
            # Complete ordered history with actors
            hist = db.query(RequestStatusHistory).filter_by(request_id=rid).order_by(
                RequestStatusHistory.id).all()
            assert [h.to_status for h in hist] == ["pending", "under_review", "accepted",
                                                  "assigned", "in_progress", "resolved"]
            assert all(h.actor_id is not None for h in hist)
            assert all(h.created_at is not None for h in hist)
            # Audit trail for every mutation
            actions = {a.action for a in db.query(AuditLog).all()}
            assert {"request.create", "request.transition", "evidence.upload",
                    "analysis.start"} <= actions
            # Both sides notified
            notes_admin = db.query(Notification).filter_by(user_id=admin["id"]).all()
            notes_officer = db.query(Notification).filter_by(user_id=officer["id"]).all()
            assert any("resolved" in n.title for n in notes_admin)
            assert any(req.code in n.title for n in notes_officer)
            # No orphans / impossible states
            assert db.query(RequestStatusHistory).filter(
                ~RequestStatusHistory.request_id.in_(
                    db.query(MunicipalRequest.id))).count() == 0
            assert db.query(Detection).filter(
                ~Detection.analysis_id.in_(db.query(Analysis.id))).count() == 0
            legal = {"pending", "under_review", "accepted", "assigned",
                     "in_progress", "resolved", "rejected"}
            assert db.query(MunicipalRequest).filter(
                ~MunicipalRequest.status.in_(legal)).count() == 0
        finally:
            db.close()
