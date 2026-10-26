"""Import side-effect: register all models on Base metadata (needed for create_all + Alembic)."""
from app.models.analysis import Analysis, Detection, Incident  # noqa: F401
from app.models.geo import Street, Video  # noqa: F401
from app.models.ops import AuditLog, Notification, RefreshToken  # noqa: F401
from app.models.request import (  # noqa: F401
    MunicipalRequest,
    OfficerAssignment,
    RequestStatusHistory,
    ResolutionEvidence,
)
from app.models.user import Organization, User  # noqa: F401
