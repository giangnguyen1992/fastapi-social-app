"""add last few column

Revision ID: 481bcf3fcaaa
Revises: 0c80400eca13
Create Date: 2022-01-14 21:36:59.008423

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "481bcf3fcaaa"
down_revision = "0c80400eca13"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        "posts",
        sa.Column("published", sa.Boolean(), nullable=False, server_default="TRUE"),
    )
    op.add_column(
        "posts",
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            nullable=False,
            server_default=sa.text("NOW()"),
        ),
    )


def downgrade():
    op.drop_column("posts", "published")
    op.drop_column("posts", "created_at")
