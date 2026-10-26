"""Analysis domain: analyses, raw detections (internal), severity, incidents."""
from datetime import datetime

from sqlalchemy import DateTime, Float, ForeignKey, Index, Integer, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base

SEVERITIES = ("weak", "medium", "critical")


class Analysis(Base):
    __tablename__ = "analyses"
    __table_args__ = (Index("ix_analyses_street_time", "street_id", "created_at"),
                      Index("ix_analyses_status_severity", "status", "overall_severity"))
    id: Mapped[int] = mapped_column(primary_key=True)
    street_id: Mapped[int] = mapped_column(ForeignKey("streets.id", ondelete="CASCADE"), index=True)
    video_id: Mapped[int | None] = mapped_column(ForeignKey("videos.id", ondelete="SET NULL"))
    created_by: Mapped[int | None] = mapped_column(ForeignKey("users.id", ondelete="SET NULL"))
    status: Mapped[str] = mapped_column(String(20), default="done", index=True)  # queued|running|done|failed
    overall_severity: Mapped[str | None] = mapped_column(String(20), nullable=True, index=True)
    weak_count: Mapped[int] = mapped_column(Integer, default=0)
    medium_count: Mapped[int] = mapped_column(Integer, default=0)
    critical_count: Mapped[int] = mapped_column(Integer, default=0)
    cat_road: Mapped[str | None] = mapped_column(String(20), nullable=True)
    cat_waste: Mapped[str | None] = mapped_column(String(20), nullable=True)
    cat_drainage: Mapped[str | None] = mapped_column(String(20), nullable=True)
    cat_infra: Mapped[str | None] = mapped_column(String(20), nullable=True)
    reason: Mapped[str | None] = mapped_column(Text, nullable=True)
    recommendation: Mapped[str | None] = mapped_column(Text, nullable=True)
    request_recommended: Mapped[bool | None] = mapped_column(nullable=True)
    reasoning_source: Mapped[str] = mapped_column(String(20), default="local")  # local reasoning engine
    error: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())


class Detection(Base):
    """Raw CV evidence — internal/audit only, never in primary UI payloads."""
    __tablename__ = "detections"
    id: Mapped[int] = mapped_column(primary_key=True)
    analysis_id: Mapped[int] = mapped_column(ForeignKey("analyses.id", ondelete="CASCADE"), index=True)
    frame_index: Mapped[int] = mapped_column(Integer)
    label: Mapped[str] = mapped_column(String(80), index=True)
    category: Mapped[str] = mapped_column(String(40), index=True)
    severity: Mapped[str] = mapped_column(String(20), index=True)
    confidence: Mapped[float] = mapped_column(Float)
    x1: Mapped[float] = mapped_column(Float)
    y1: Mapped[float] = mapped_column(Float)
    x2: Mapped[float] = mapped_column(Float)
    y2: Mapped[float] = mapped_column(Float)
    frame_width: Mapped[float | None] = mapped_column(Float, nullable=True)  # px, None = unknown
    frame_height: Mapped[float | None] = mapped_column(Float, nullable=True)
    mask_area: Mapped[float | None] = mapped_column(Float, nullable=True)  # frame fraction 0..1
    mask_polygon: Mapped[str | None] = mapped_column(Text, nullable=True)  # compact JSON ≤32 pts


class Incident(Base):
    __tablename__ = "incidents"
    id: Mapped[int] = mapped_column(primary_key=True)
    analysis_id: Mapped[int] = mapped_column(ForeignKey("analyses.id", ondelete="CASCADE"), unique=True)
    street_id: Mapped[int] = mapped_column(ForeignKey("streets.id", ondelete="CASCADE"), index=True)
    severity: Mapped[str] = mapped_column(String(20), index=True)
    status: Mapped[str] = mapped_column(String(20), default="open", index=True)  # open | requested | resolved
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
