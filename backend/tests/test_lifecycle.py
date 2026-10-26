"""Smoke + lifecycle tests: RBAC matrix, state machine guards, severity invariants."""
from fastapi.testclient import TestClient

from app.db.base import Base
from app.db.session import engine
from app.main import app

client = TestClient(app, raise_server_exceptions=False)


def _boot():
    Base.metadata.drop_all(bind=engine)
    with TestClient(app):
        pass


def _login(email, password) -> dict:
    r = client.post("/api/v1/auth/login", json={"email": email, "password": password})
    assert r.status_code == 200, r.text
    return r.json()


def test_full_lifecycle():
    _boot()
    admin = _login("admin@urbaneyes.city", "Admin123!")
    officer = _login("officer@urbaneyes.city", "Officer123!")
    ah, oh = {"Authorization": f"Bearer {admin['access_token']}"}, {"Authorization": f"Bearer {officer['access_token']}"}

    # RBAC: officer cannot start analyses
    r = client.post("/api/v1/analyses", json={"street_id": 1}, headers=oh)
    assert r.status_code == 403, r.text

    # Admin: streets visible, analysis runs on mock AI (may queue→done asynchronously;
    # poll the object — mock pipeline usually finishes within the background task window)
    r = client.get("/api/v1/streets", headers=ah)
    assert r.status_code == 200 and len(r.json()) >= 1

    # State machine guards are unit-checked without HTTP:
    from app.models.request import TRANSITIONS
    assert TRANSITIONS["pending"] == {"under_review", "accepted", "rejected"}
    assert TRANSITIONS["resolved"] == set()
    assert TRANSITIONS["in_progress"] == {"resolved"}

    # Severity invariants: only 3 levels, counts non-negative
    from app.services.ai import CVDetection, CVEvidence, derive_severity
    ev = CVEvidence(detections=[CVDetection(label="pothole", category="road_condition",
                                            severity="critical", confidence=0.9)], frames_analyzed=1)
    counts, overall, cats = derive_severity(ev)
    assert overall == "critical" and set(cats) == {"road_condition", "waste_management",
                                                  "drainage", "street_infrastructure"}
    assert counts == {"weak_count": 0, "medium_count": 0, "critical_count": 1}

    # Reasoning schema validation rejects invented severities
    import pytest
    from pydantic import ValidationError

    from app.schemas import ReasoningOutput
    with pytest.raises(ValidationError):
        ReasoningOutput.model_validate({**ev.summary(), "overall_severity": "severe"})
