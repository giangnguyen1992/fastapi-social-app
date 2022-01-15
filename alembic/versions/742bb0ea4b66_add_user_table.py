"""add user table

Revision ID: 742bb0ea4b66
Revises: 9e2b36bf01fe
Create Date: 2022-01-14 21:27:43.680658

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "742bb0ea4b66"
down_revision = "9e2b36bf01fe"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("email", sa.String(), nullable=False),
        sa.Column("password", sa.String(), nullable=False),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
    )


def downgrade():
    op.drop_table("users")
