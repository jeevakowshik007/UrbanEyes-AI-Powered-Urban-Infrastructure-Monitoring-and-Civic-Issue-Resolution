"""Pydantic contracts. Severity is ALWAYS Literal['weak','medium','critical'] — no other values."""
from datetime import datetime
from typing import Literal

from pydantic import BaseModel, EmailStr, Field

Severity = Literal["weak", "medium", "critical"]
RequestStatus = Literal["pending", "under_review", "accepted", "assigned", "in_progress", "resolved", "rejected"]
Role = Literal["admin", "officer"]

CATEGORIES = ("road_condition", "waste_management", "drainage", "street_infrastructure")


# ---------- Auth ----------
class RegisterIn(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=128)
    full_name: str = Field(min_length=2, max_length=160)
    role: Role = "admin"


class LoginIn(BaseModel):
    email: EmailStr
    password: str


class TokenOut(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"  # noqa: S105 — not a credential, just the OAuth2 scheme label


class UserOut(BaseModel):
    id: int
    email: str
    full_name: str
    role: str
    org_id: int | None = None


# ---------- Streets / videos ----------
class StreetOut(BaseModel):
    id: int
    name: str
    area: str
    latitude: float
    longitude: float
    video_count: int = 0
    latest_severity: Severity | None = None
    latest_analysis_at: datetime | None = None

    model_config = {"from_attributes": True}


class VideoOut(BaseModel):
    id: int
    street_id: int
    filename: str
    storage_key: str
    size_bytes: int
    duration_s: float | None
    status: str
    created_at: datetime

    model_config = {"from_attributes": True}


# ---------- Analyses (user-facing: severity counts, never raw object counts) ----------
class AnalysisCreate(BaseModel):
    street_id: int
    video_id: int | None = None


class CategorySeverity(BaseModel):
    road_condition: Severity
    waste_management: Severity
    drainage: Severity
    street_infrastructure: Severity


class ReasoningOutput(BaseModel):
    """Strict validated output of the Local Urban Infrastructure Reasoning Engine."""
    overall_severity: Severity
    weak_count: int = Field(ge=0)
    medium_count: int = Field(ge=0)
    critical_count: int = Field(ge=0)
    categories: CategorySeverity
    reason: str = Field(min_length=10, max_length=4000)
    recommendation: str = Field(min_length=10, max_length=4000)
    municipal_request_recommended: bool


class AnalysisOut(BaseModel):
    id: int
    street_id: int
    video_id: int | None
    status: str
    overall_severity: Severity | None = None
    weak_count: int
    medium_count: int
    critical_count: int
    categories: dict | None = None
    reason: str | None = None
    recommendation: str | None = None
    request_recommended: bool | None = None
    reasoning_source: str
    created_at: datetime

    model_config = {"from_attributes": True}


class IncidentOut(BaseModel):
    id: int
    analysis_id: int
    street_id: int
    severity: Severity
    status: str
    created_at: datetime

    model_config = {"from_attributes": True}


# ---------- Requests ----------
class RequestCreate(BaseModel):
    analysis_id: int
    note: str | None = Field(default=None, max_length=2000)


class StatusPatch(BaseModel):
    to_status: RequestStatus
    reason: str | None = Field(default=None, max_length=2000)


class AssignIn(BaseModel):
    officer_id: int


class RequestOut(BaseModel):
    id: int
    code: str
    incident_id: int
    analysis_id: int
    street_id: int
    submitted_by: int
    assigned_to: int | None
    status: str
    severity: Severity
    note: str | None
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}


class HistoryOut(BaseModel):
    id: int
    request_id: int
    actor_id: int | None
    from_status: str | None
    to_status: str
    reason: str | None
    created_at: datetime

    model_config = {"from_attributes": True}


# ---------- Misc ----------
class NotificationOut(BaseModel):
    id: int
    title: str
    body: str
    kind: str
    is_read: bool
    created_at: datetime

    model_config = {"from_attributes": True}


class EvidenceOut(BaseModel):
    id: int
    request_id: int
    officer_id: int
    kind: str
    storage_key: str
    notes: str | None
    created_at: datetime

    model_config = {"from_attributes": True}


class StreetRef(BaseModel):
    id: int
    name: str
    area: str


class RequestRef(BaseModel):
    id: int
    code: str
    status: str


class SearchOut(BaseModel):
    streets: list[StreetRef]
    requests: list[RequestRef]


class DashboardOut(BaseModel):
    critical_analyses: int
    total_analyses: int
    open_requests: int
    requests_by_status: dict[str, int]
    recent_analysis_ids: list[int]
