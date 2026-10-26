"""Evidence enrichment: real frame dimensions + segmentation mask columns on detections."""
from collections.abc import Sequence

import sqlalchemy as sa

from alembic import op

revision: str = "0002_detection_evidence"
down_revision: str = "0001_initial"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.add_column("detections", sa.Column("frame_width", sa.Float(), nullable=True))
    op.add_column("detections", sa.Column("frame_height", sa.Float(), nullable=True))
    op.add_column("detections", sa.Column("mask_area", sa.Float(), nullable=True))
    op.add_column("detections", sa.Column("mask_polygon", sa.Text(), nullable=True))


def downgrade() -> None:
    for col in ("mask_polygon", "mask_area", "frame_height", "frame_width"):
        op.drop_column("detections", col)
