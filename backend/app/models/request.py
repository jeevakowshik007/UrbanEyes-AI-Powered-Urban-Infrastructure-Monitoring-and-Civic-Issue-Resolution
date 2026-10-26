"""Request lifecycle: municipal_requests + history + assignments + evidence."""
from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Index, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base

STATUSES = ("pending", "under_review", "accepted", "assigned", "in_progress", "resolved", "rejected")

# Legal transitions for the auditable state machine.
TRANSITIONS: dict[str, set[str]] = {
    "pending": {"under_review", "accepted", "rejected"},
    "under_review": {"accepted", "rejected"},
    "accepted": {"assigned", "rejected"},
    "assigned": {"in_progress", "assigned"},
    "in_progress": {"resolved"},
    "rejected": set(),
    "resolved": set(),
}


class MunicipalRequest(Base):
    __tablename__ = "municipal_requests"
    __table_args__ = (Index("ix_requests_street_status", "street_id", "status"),
                      Index("ix_requests_assigned_status", "assigned_to", "status"))
    id: Mapped[int] = mapped_column(primary_key=True)
    code: Mapped[str] = mapped_column(String(24), unique=True, index=True)  # UE-2026-0001
    incident_id: Mapped[int] = mapped_column(ForeignKey("incidents.id", ondelete="CASCADE"))
    analysis_id: Mapped[int] = mapped_column(ForeignKey("analyses.id", ondelete="CASCADE"))
    street_id: Mapped[int] = mapped_column(ForeignKey("streets.id", ondelete="CASCADE"), index=True)
    submitted_by: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="SET NULL"))
    assigned_to: Mapped[int | None] = mapped_column(ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    status: Mapped[str] = mapped_column(String(20), default="pending", index=True)
    severity: Mapped[str] = mapped_column(String(20), index=True)
    note: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())


class RequestStatusHistory(Base):
    __tablename__ = "request_status_history"
    __table_args__ = (Index("ix_history_request_time", "request_id", "created_at"),)
    id: Mapped[int] = mapped_column(primary_key=True)
    request_id: Mapped[int] = mapped_column(ForeignKey("municipal_requests.id", ondelete="CASCADE"), index=True)
    actor_id: Mapped[int | None] = mapped_column(ForeignKey("users.id", ondelete="SET NULL"))
    from_status: Mapped[str | None] = mapped_column(String(20), nullable=True)
    to_status: Mapped[str] = mapped_column(String(20))
    reason: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())


class OfficerAssignment(Base):
    __tablename__ = "officer_assignments"
    id: Mapped[int] = mapped_column(primary_key=True)
    request_id: Mapped[int] = mapped_column(ForeignKey("municipal_requests.id", ondelete="CASCADE"), index=True)
    officer_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), index=True)
    assigned_by: Mapped[int | None] = mapped_column(ForeignKey("users.id", ondelete="SET NULL"))
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())


class ResolutionEvidence(Base):
    __tablename__ = "resolution_evidence"
    id: Mapped[int] = mapped_column(primary_key=True)
    request_id: Mapped[int] = mapped_column(ForeignKey("municipal_requests.id", ondelete="CASCADE"), index=True)
    officer_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="SET NULL"))
    kind: Mapped[str] = mapped_column(String(20))  # before | after | repair
    storage_key: Mapped[str] = mapped_column(String(512))
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
