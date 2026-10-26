"""Adversarial tests: auth bypass, role escalation, bad IDs, bad JSON,
token forgery/expiry, assignment abuse, rejection flow, no-auto-create."""
from fastapi.testclient import TestClient
from jose import jwt

from app.core.config import get_settings
from app.db.base import Base
from app.db.session import SessionLocal, engine
from app.main import app
from app.models.analysis import Analysis, Incident


def _client():
    Base.metadata.drop_all(bind=engine)
    return TestClient(app)


def _login(c, email, pw):
    r = c.post("/api/v1/auth/login", json={"email": email, "password": pw})
    assert r.status_code == 200, r.text
    return r.json()


def _admin_headers(c):
    t = _login(c, "admin@urbaneyes.city", "Admin123!")
    return {"Authorization": f"Bearer {t['access_token']}"}, t


def _officer_headers(c):
    t = _login(c, "officer@urbaneyes.city", "Officer123!")
    return {"Authorization": f"Bearer {t['access_token']}"}, t


def _done_analysis(db, street_id=1):
    a = Analysis(street_id=street_id, video_id=None, created_by=1, status="done",
                 overall_severity="critical", weak_count=0, medium_count=1, critical_count=2,
                 cat_road="critical", cat_waste="weak", cat_drainage="weak", cat_infra="weak",
                 reason="r" * 20, recommendation="rec" * 20, request_recommended=True,
                 reasoning_source="local")
    db.add(a)
    db.flush()
    db.add(Incident(analysis_id=a.id, street_id=street_id, severity="critical"))
    db.commit()
    db.refresh(a)
    return a


def test_unauthenticated_rejected():
    with _client() as c:
        for method, path, kw in [
            ("get", "/api/v1/streets", {}),
            ("get", "/api/v1/analyses", {}),
            ("get", "/api/v1/requests", {}),
            ("get", "/api/v1/notifications", {}),
            ("get", "/api/v1/dashboard", {}),
            ("get", "/api/v1/search?q=ab", {}),
            ("get", "/api/v1/files?key=videos/x.mp4", {}),
            ("post", "/api/v1/analyses", {"json": {"street_id": 1}}),
            ("post", "/api/v1/requests", {"json": {"analysis_id": 1}}),
            ("patch", "/api/v1/requests/1/status", {"json": {"to_status": "accepted"}}),
        ]:
            r = getattr(c, method)(path, **kw)
            assert r.status_code == 401, (method, path, r.status_code)


def test_cross_role_forbidden():
    with _client() as c:
        oh, _ = _officer_headers(c)
        assert c.post("/api/v1/analyses", json={"street_id": 1}, headers=oh).status_code == 403
        assert c.post("/api/v1/videos/upload?street_id=1",
                      files={"file": ("x.mp4", b"data", "video/mp4")}, headers=oh).status_code == 403
        assert c.post("/api/v1/requests", json={"analysis_id": 1}, headers=oh).status_code == 403
        assert c.patch("/api/v1/requests/999/status",
                       json={"to_status": "accepted"}, headers=oh).status_code in (403, 404)
        ah, _ = _admin_headers(c)
        assert c.patch("/api/v1/requests/999/status",
                       json={"to_status": "accepted"}, headers=ah).status_code == 403
        assert c.post("/api/v1/requests/999/assignments",
                      json={"officer_id": 2}, headers=ah).status_code == 403


def test_invalid_ids_and_malformed_json():
    with _client() as c:
        ah, _ = _admin_headers(c)
        oh, _ = _officer_headers(c)
        assert c.get("/api/v1/requests/abc", headers=ah).status_code == 422
        assert c.get("/api/v1/streets/99999", headers=ah).status_code == 404
        assert c.get("/api/v1/analyses/99999", headers=ah).status_code == 404
        assert c.patch("/api/v1/requests/99999/status",
                       json={"to_status": "accepted"}, headers=oh).status_code == 404
        assert c.post("/api/v1/auth/login", json={"email": 123, "password": "x"}).status_code == 422
        assert c.post("/api/v1/requests", json={}, headers=ah).status_code == 422
        assert c.post("/api/v1/auth/register",
                      json={"email": "z@urbaneyes.city", "password": "Password1!",
                            "full_name": "Zed", "role": "superadmin"}).status_code == 422


def _forge(sub, role, secret, exp_seconds=900):
    import time
    s = get_settings()
    return jwt.encode({"sub": sub, "role": role, "typ": "access",
                       "iat": int(time.time()), "exp": int(time.time()) + exp_seconds},
                      secret, algorithm=s.JWT_ALGORITHM)


def test_expired_and_forged_tokens_rejected():
    with _client() as c:
        s = get_settings()
        expired = _forge("admin@urbaneyes.city", "admin", s.JWT_SECRET, exp_seconds=-10)
        assert c.get("/api/v1/auth/me", headers={"Authorization": f"Bearer {expired}"}).status_code == 401
        forged = _forge("admin@urbaneyes.city", "admin", "wrong-secret")
        assert c.get("/api/v1/auth/me", headers={"Authorization": f"Bearer {forged}"}).status_code == 401


def test_role_claim_in_token_is_ignored():
    """RBAC comes from the database user, never from the client-presented role claim."""
    with _client() as c:
        s = get_settings()
        escalated = _forge("officer@urbaneyes.city", "admin", s.JWT_SECRET)
        r = c.post("/api/v1/analyses", json={"street_id": 1},
                   headers={"Authorization": f"Bearer {escalated}"})
        assert r.status_code == 403


def test_assignment_abuse():
    with _client() as c:
        ah, _ = _admin_headers(c)
        oh, _ = _officer_headers(c)
        me_admin = c.get("/api/v1/auth/me", headers=ah).json()
        db = SessionLocal()
        try:
            a = _done_analysis(db)
            req = c.post("/api/v1/requests", json={"analysis_id": a.id}, headers=ah).json()
        finally:
            db.close()
        # Assigning a non-officer (admin) or ghost id must fail
        assert c.post(f"/api/v1/requests/{req['id']}/assignments",
                      json={"officer_id": me_admin["id"]}, headers=oh).status_code == 404
        assert c.post(f"/api/v1/requests/{req['id']}/assignments",
                      json={"officer_id": 99999}, headers=oh).status_code == 404


def test_rejection_flow_and_terminal_state():
    with _client() as c:
        ah, _ = _admin_headers(c)
        oh, _ = _officer_headers(c)
        db = SessionLocal()
        try:
            a = _done_analysis(db)
            req = c.post("/api/v1/requests", json={"analysis_id": a.id}, headers=ah).json()
        finally:
            db.close()
        rid = req["id"]
        assert c.patch(f"/api/v1/requests/{rid}/status",
                       json={"to_status": "rejected"}, headers=oh).status_code == 422
        r = c.patch(f"/api/v1/requests/{rid}/status",
                    json={"to_status": "rejected", "reason": "Duplicate of UE-2026-0001"}, headers=oh)
        assert r.status_code == 200 and r.json()["status"] == "rejected"
        assert c.patch(f"/api/v1/requests/{rid}/status",
                       json={"to_status": "accepted"}, headers=oh).status_code == 409


def test_critical_never_auto_creates_request():
    with _client() as c:
        ah, _ = _admin_headers(c)
        db = SessionLocal()
        try:
            _done_analysis(db)
            before = c.get("/api/v1/requests", headers=ah).json()
        finally:
            db.close()
        assert before == []
