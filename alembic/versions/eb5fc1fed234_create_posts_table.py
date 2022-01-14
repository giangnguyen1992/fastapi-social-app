"""create posts table

Revision ID: eb5fc1fed234
Revises: 
Create Date: 2022-01-14 20:58:31.973119

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "eb5fc1fed234"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "posts",
        sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
        sa.Column("title", sa.String(), nullable=False),
    )


def downgrade():
    op.drop_table("posts")
