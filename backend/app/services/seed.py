"""Demo seed: org + admin + officer + 4 streets + 1 video marker each.
Runs on startup when SEED_DEMO=true and users table is empty."""
from sqlalchemy.orm import Session

from app.core.security import hash_password
from app.models.geo import Street
from app.models.user import Organization, User

STREETS = [
    ("MG Road", "Central", 12.9716, 77.5946),
    ("Brigade Road", "Central", 12.9757, 77.6013),
    ("Outer Ring Road", "East", 12.9698, 77.7499),
    ("Kanakapura Road", "South", 12.9077, 77.5851),
]


def seed_demo(db: Session) -> None:
    if db.query(User).count():
        return
    org = Organization(name="City Municipal Corporation", type="municipal")
    db.add(org)
    db.flush()
    db.add(User(email="admin@urbaneyes.city", password_hash=hash_password("Admin123!"),
                full_name="City Administrator", role="admin", org_id=org.id))
    db.add(User(email="officer@urbaneyes.city", password_hash=hash_password("Officer123!"),
                full_name="Field Officer", role="officer", org_id=org.id))
    for name, area, lat, lon in STREETS:
        db.add(Street(name=name, area=area, latitude=lat, longitude=lon))
    db.commit()
