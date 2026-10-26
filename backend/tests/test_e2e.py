"""Full operational flow: admin analyze → confirm request → officer lifecycle → resolve."""
import time

from fastapi.testclient import TestClient

from app.db.base import Base
from app.db.session import engine
from app.main import app


def _login(c, email, pw):
    r = c.post("/api/v1/auth/login", json={"email": email, "password": pw})
    assert r.status_code == 200, r.text
    return {"Authorization": f"Bearer {r.json()['access_token']}"}


def test_end_to_end():
    Base.metadata.drop_all(bind=engine)
    with TestClient(app) as c:
        ah = _login(c, "admin@urbaneyes.city", "Admin123!")
        oh = _login(c, "officer@urbaneyes.city", "Officer123!")

        streets = c.get("/api/v1/streets", headers=ah).json()
        assert len(streets) == 4
        sid = streets[0]["id"]

        # No video yet → 422 with clear message (no fake analysis)
        r = c.post("/api/v1/analyses", json={"street_id": sid}, headers=ah)
        assert r.status_code == 422, r.text

        # Upload a tiny synthetic mp4 (generated via OpenCV) → analyze → poll done
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
            r = c.post("/api/v1/videos/upload", params={"street_id": sid},
                       files={"file": ("street.mp4", f, "video/mp4")}, headers=ah)
        os.remove(tmp)
        assert r.status_code == 201, r.text

        r = c.post("/api/v1/analyses", json={"street_id": sid}, headers=ah)
        assert r.status_code == 202, r.text
        aid = r.json()["analysis_id"]
        for _ in range(60):
            a = c.get(f"/api/v1/analyses/{aid}", headers=ah).json()
            if a["status"] in ("done", "failed"):
                break
            time.sleep(0.5)
        assert a["status"] == "done", a
        assert a["overall_severity"] in ("weak", "medium", "critical")
        assert set(a["categories"]) == {"road_condition", "waste_management",
                                        "drainage", "street_infrastructure"}

        # Admin explicitly confirms → request created (never automatic)
        r = c.post("/api/v1/requests", json={"analysis_id": aid, "note": "please inspect"}, headers=ah)
        assert r.status_code == 201, r.text
        req = r.json()
        assert req["status"] == "pending" and req["code"].startswith("UE-")

        # Officer: illegal jump pending → resolved rejected
        r = c.patch(f"/api/v1/requests/{req['id']}/status",
                    json={"to_status": "resolved"}, headers=oh)
        assert r.status_code == 409, r.text

        # Legal path with evidence gate
        for st, reason in [("under_review", None), ("accepted", None), ("assigned", None)]:
            if st == "assigned":
                me = c.get("/api/v1/auth/me", headers=oh).json()
                r = c.post(f"/api/v1/requests/{req['id']}/assignments",
                           json={"officer_id": me["id"]}, headers=oh)
                assert r.status_code == 200, r.text
                continue
            r = c.patch(f"/api/v1/requests/{req['id']}/status",
                        json={"to_status": st, "reason": reason}, headers=oh)
            assert r.status_code == 200, r.text
        r = c.patch(f"/api/v1/requests/{req['id']}/status",
                    json={"to_status": "in_progress"}, headers=oh)
        assert r.status_code == 200, r.text
        # Resolve without evidence → 422
        r = c.patch(f"/api/v1/requests/{req['id']}/status",
                    json={"to_status": "resolved"}, headers=oh)
        assert r.status_code == 422, r.text
        # Upload after-evidence → resolve OK
        r = c.post(f"/api/v1/requests/{req['id']}/evidence?kind=after",
                   files={"file": ("after.jpg", b"\xff\xd8\xff\xe0" + b"\x00" * 32, "image/jpeg")}, headers=oh)
        assert r.status_code == 201, r.text
        r = c.patch(f"/api/v1/requests/{req['id']}/status",
                    json={"to_status": "resolved"}, headers=oh)
        assert r.status_code == 200 and r.json()["status"] == "resolved", r.text

        # History is complete + admin got notified
        hist = c.get(f"/api/v1/requests/{req['id']}/history", headers=ah).json()
        assert [h["to_status"] for h in hist] == ["pending", "under_review", "accepted",
                                                 "assigned", "in_progress", "resolved"]
        notes = c.get("/api/v1/notifications", headers=ah).json()
        assert any("resolved" in n["title"] for n in notes)
        dash = c.get("/api/v1/dashboard", headers=ah).json()
        assert dash["total_analyses"] >= 1 and dash["requests_by_status"]["resolved"] >= 1
