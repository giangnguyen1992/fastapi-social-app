"""add content column

Revision ID: 9e2b36bf01fe
Revises: eb5fc1fed234
Create Date: 2022-01-14 21:24:04.421925

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "9e2b36bf01fe"
down_revision = "eb5fc1fed234"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))


def downgrade():
    op.drop_column("posts", "content")
