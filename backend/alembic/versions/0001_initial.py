"""Initial schema — mirrors the SQLAlchemy models + docs/DATABASE_SCHEMA.md.

CHECK constraints mirror infra/postgres_init.sql (severity: 3 levels, request
status: 7 states). Safe on Postgres and SQLite.
"""
from collections.abc import Sequence

import sqlalchemy as sa

from alembic import op

revision: str = "0001_initial"
down_revision: str | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None

DET_SEV = sa.CheckConstraint("severity IN ('weak','medium','critical')", name="ck_det_severity3")
REQ_STATUS = sa.CheckConstraint(
    "status IN ('pending','under_review','accepted','assigned','in_progress','resolved','rejected')",
    name="ck_request_status7")


def upgrade() -> None:
    op.create_table(
        "organizations",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("name", sa.String(160), nullable=False, unique=True),
        sa.Column("type", sa.String(40), nullable=False, server_default="municipal"),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
    )
    op.create_index("ix_organizations_name", "organizations", ["name"])

    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("email", sa.String(255), nullable=False, unique=True),
        sa.Column("password_hash", sa.String(255), nullable=False),
        sa.Column("full_name", sa.String(160), nullable=False),
        sa.Column("role", sa.String(20), nullable=False),
        sa.Column("org_id", sa.Integer(), sa.ForeignKey("organizations.id", ondelete="SET NULL")),
        sa.Column("is_active", sa.Boolean(), nullable=False, server_default=sa.true()),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.CheckConstraint("role IN ('admin','officer')", name="ck_users_role"),
    )
    op.create_index("ix_users_email", "users", ["email"])
    op.create_index("ix_users_role", "users", ["role"])

    op.create_table(
        "streets",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("name", sa.String(200), nullable=False),
        sa.Column("area", sa.String(200), nullable=False, server_default=""),
        sa.Column("latitude", sa.Float(), nullable=False),
        sa.Column("longitude", sa.Float(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
    )
    op.create_index("ix_streets_name", "streets", ["name"])
    op.create_index("ix_streets_area", "streets", ["area"])

    op.create_table(
        "videos",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("street_id", sa.Integer(), sa.ForeignKey("streets.id", ondelete="CASCADE"), nullable=False),
        sa.Column("storage_key", sa.String(512), nullable=False),
        sa.Column("filename", sa.String(255), nullable=False),
        sa.Column("size_bytes", sa.Integer(), nullable=False),
        sa.Column("duration_s", sa.Float(), nullable=True),
        sa.Column("status", sa.String(20), nullable=False, server_default="ready"),
        sa.Column("recorded_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.CheckConstraint("status IN ('ready','invalid')", name="ck_videos_status"),
    )
    op.create_index("ix_videos_street_id", "videos", ["street_id"])

    op.create_table(
        "analyses",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("street_id", sa.Integer(), sa.ForeignKey("streets.id", ondelete="CASCADE"), nullable=False),
        sa.Column("video_id", sa.Integer(), sa.ForeignKey("videos.id", ondelete="SET NULL"), nullable=True),
        sa.Column("created_by", sa.Integer(), sa.ForeignKey("users.id", ondelete="SET NULL"), nullable=True),
        sa.Column("status", sa.String(20), nullable=False, server_default="done"),
        sa.Column("overall_severity", sa.String(20), nullable=True),
        sa.Column("weak_count", sa.Integer(), nullable=False, server_default="0"),
        sa.Column("medium_count", sa.Integer(), nullable=False, server_default="0"),
        sa.Column("critical_count", sa.Integer(), nullable=False, server_default="0"),
        sa.Column("cat_road", sa.String(20), nullable=True),
        sa.Column("cat_waste", sa.String(20), nullable=True),
        sa.Column("cat_drainage", sa.String(20), nullable=True),
        sa.Column("cat_infra", sa.String(20), nullable=True),
        sa.Column("reason", sa.Text(), nullable=True),
        sa.Column("recommendation", sa.Text(), nullable=True),
        sa.Column("request_recommended", sa.Boolean(), nullable=True),
        sa.Column("reasoning_source", sa.String(20), nullable=False, server_default="local"),
        sa.Column("error", sa.Text(), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.CheckConstraint("status IN ('queued','running','done','failed')", name="ck_analyses_status"),
        sa.CheckConstraint("overall_severity IS NULL OR overall_severity IN ('weak','medium','critical')",
                           name="ck_analyses_severity"),
        sa.CheckConstraint("reasoning_source = 'local'", name="ck_analyses_reasoning_source"),
    )
    op.create_index("ix_analyses_street_id", "analyses", ["street_id"])
    op.create_index("ix_analyses_status", "analyses", ["status"])
    op.create_index("ix_analyses_overall_severity", "analyses", ["overall_severity"])
    op.create_index("ix_analyses_street_time", "analyses", ["street_id", "created_at"])
    op.create_index("ix_analyses_status_severity", "analyses", ["status", "overall_severity"])

    op.create_table(
        "detections",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("analysis_id", sa.Integer(), sa.ForeignKey("analyses.id", ondelete="CASCADE"), nullable=False),
        sa.Column("frame_index", sa.Integer(), nullable=False),
        sa.Column("label", sa.String(80), nullable=False),
        sa.Column("category", sa.String(40), nullable=False),
        sa.Column("severity", sa.String(20), nullable=False),
        sa.Column("confidence", sa.Float(), nullable=False),
        sa.Column("x1", sa.Float(), nullable=False),
        sa.Column("y1", sa.Float(), nullable=False),
        sa.Column("x2", sa.Float(), nullable=False),
        sa.Column("y2", sa.Float(), nullable=False),
        DET_SEV,
    )
    op.create_index("ix_detections_analysis_id", "detections", ["analysis_id"])
    op.create_index("ix_detections_label", "detections", ["label"])
    op.create_index("ix_detections_category", "detections", ["category"])
    op.create_index("ix_detections_severity", "detections", ["severity"])

    op.create_table(
        "incidents",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("analysis_id", sa.Integer(), sa.ForeignKey("analyses.id", ondelete="CASCADE"),
                  nullable=False, unique=True),
        sa.Column("street_id", sa.Integer(), sa.ForeignKey("streets.id", ondelete="CASCADE"), nullable=False),
        sa.Column("severity", sa.String(20), nullable=False),
        sa.Column("status", sa.String(20), nullable=False, server_default="open"),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.CheckConstraint("severity IN ('weak','medium','critical')", name="ck_incidents_severity"),
        sa.CheckConstraint("status IN ('open','requested','resolved')", name="ck_incidents_status"),
    )
    op.create_index("ix_incidents_street_id", "incidents", ["street_id"])
    op.create_index("ix_incidents_severity", "incidents", ["severity"])
    op.create_index("ix_incidents_status", "incidents", ["status"])

    op.create_table(
        "municipal_requests",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("code", sa.String(24), nullable=False, unique=True),
        sa.Column("incident_id", sa.Integer(), sa.ForeignKey("incidents.id", ondelete="CASCADE"), nullable=False),
        sa.Column("analysis_id", sa.Integer(), sa.ForeignKey("analyses.id", ondelete="CASCADE"), nullable=False),
        sa.Column("street_id", sa.Integer(), sa.ForeignKey("streets.id", ondelete="CASCADE"), nullable=False),
        sa.Column("submitted_by", sa.Integer(), sa.ForeignKey("users.id", ondelete="SET NULL"), nullable=False),
        sa.Column("assigned_to", sa.Integer(), sa.ForeignKey("users.id", ondelete="SET NULL"), nullable=True),
        sa.Column("status", sa.String(20), nullable=False, server_default="pending"),
        sa.Column("severity", sa.String(20), nullable=False),
        sa.Column("note", sa.Text(), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.CheckConstraint("severity IN ('weak','medium','critical')", name="ck_requests_severity"),
        REQ_STATUS,
    )
    op.create_index("ix_municipal_requests_code", "municipal_requests", ["code"])
    op.create_index("ix_municipal_requests_street_id", "municipal_requests", ["street_id"])
    op.create_index("ix_municipal_requests_status", "municipal_requests", ["status"])
    op.create_index("ix_municipal_requests_severity", "municipal_requests", ["severity"])
    op.create_index("ix_requests_street_status", "municipal_requests", ["street_id", "status"])
    op.create_index("ix_requests_assigned_status", "municipal_requests", ["assigned_to", "status"])

    op.create_table(
        "request_status_history",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("request_id", sa.Integer(), sa.ForeignKey("municipal_requests.id", ondelete="CASCADE"),
                  nullable=False),
        sa.Column("actor_id", sa.Integer(), sa.ForeignKey("users.id", ondelete="SET NULL"), nullable=True),
        sa.Column("from_status", sa.String(20), nullable=True),
        sa.Column("to_status", sa.String(20), nullable=False),
        sa.Column("reason", sa.Text(), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
    )
    op.create_index("ix_history_request_id", "request_status_history", ["request_id"])
    op.create_index("ix_history_request_time", "request_status_history", ["request_id", "created_at"])

    op.create_table(
        "officer_assignments",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("request_id", sa.Integer(), sa.ForeignKey("municipal_requests.id", ondelete="CASCADE"),
                  nullable=False),
        sa.Column("officer_id", sa.Integer(), sa.ForeignKey("users.id", ondelete="CASCADE"), nullable=False),
        sa.Column("assigned_by", sa.Integer(), sa.ForeignKey("users.id", ondelete="SET NULL"), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
    )
    op.create_index("ix_assignments_request_id", "officer_assignments", ["request_id"])
    op.create_index("ix_assignments_officer_id", "officer_assignments", ["officer_id"])

    op.create_table(
        "resolution_evidence",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("request_id", sa.Integer(), sa.ForeignKey("municipal_requests.id", ondelete="CASCADE"),
                  nullable=False),
        sa.Column("officer_id", sa.Integer(), sa.ForeignKey("users.id", ondelete="SET NULL"), nullable=False),
        sa.Column("kind", sa.String(20), nullable=False),
        sa.Column("storage_key", sa.String(512), nullable=False),
        sa.Column("notes", sa.Text(), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.CheckConstraint("kind IN ('before','after','repair')", name="ck_evidence_kind"),
    )
    op.create_index("ix_evidence_request_id", "resolution_evidence", ["request_id"])

    op.create_table(
        "notifications",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("user_id", sa.Integer(), sa.ForeignKey("users.id", ondelete="CASCADE"), nullable=False),
        sa.Column("title", sa.String(200), nullable=False),
        sa.Column("body", sa.Text(), nullable=False, server_default=""),
        sa.Column("kind", sa.String(40), nullable=False, server_default="info"),
        sa.Column("is_read", sa.Boolean(), nullable=False, server_default=sa.false()),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
    )
    op.create_index("ix_notifications_user_id", "notifications", ["user_id"])
    op.create_index("ix_notifications_is_read", "notifications", ["is_read"])
    op.create_index("ix_notifications_user_time", "notifications", ["user_id", "created_at"])

    op.create_table(
        "audit_logs",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("actor_id", sa.Integer(), sa.ForeignKey("users.id", ondelete="SET NULL"), nullable=True),
        sa.Column("action", sa.String(80), nullable=False),
        sa.Column("entity", sa.String(80), nullable=False),
        sa.Column("entity_id", sa.String(80), nullable=False),
        sa.Column("meta_json", sa.Text(), nullable=False, server_default="{}"),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
    )
    op.create_index("ix_audit_action", "audit_logs", ["action"])
    op.create_index("ix_audit_entity", "audit_logs", ["entity"])

    op.create_table(
        "refresh_tokens",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("user_id", sa.Integer(), sa.ForeignKey("users.id", ondelete="CASCADE"), nullable=False),
        sa.Column("jti", sa.String(64), nullable=False, unique=True),
        sa.Column("revoked", sa.Boolean(), nullable=False, server_default=sa.false()),
        sa.Column("expires_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
    )
    op.create_index("ix_refresh_user_id", "refresh_tokens", ["user_id"])
    op.create_index("ix_refresh_jti", "refresh_tokens", ["jti"])
    op.create_index("ix_refresh_user_expiry", "refresh_tokens", ["user_id", "expires_at"])


def downgrade() -> None:
    for table in ("refresh_tokens", "audit_logs", "notifications", "resolution_evidence",
                  "officer_assignments", "request_status_history", "municipal_requests",
                  "incidents", "detections", "analyses", "videos", "streets", "users",
                  "organizations"):
        op.drop_table(table)
