"""create_polls_table

Revision ID: fc30b71b7597
Revises: 59f1b4b04607
Create Date: 2022-02-18 07:24:35.321087

"""
import enum
from alembic import op
import sqlalchemy as sa


class PollType(enum.Enum):
    text = 1
    image = 2

# revision identifiers, used by Alembic.
revision = 'fc30b71b7597'
down_revision = '59f1b4b04607'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
    'polls',
    sa.Column('id', sa.Integer()),
    sa.Column('title', sa.String(length=30), nullable=False),
    sa.Column('type',sa.Enum(PollType), nullable=False),
    sa.Column('is_add_choices_active', sa.Boolean, nullable=False),
    sa.Column('is_voting_active', sa.Boolean, nullable=False),
    sa.Column('created_by', sa.Integer, nullable=False),
    sa.Column('created_at', sa.DateTime, nullable=False),
    sa.Column('updated_at', sa.DateTime, nullable=False),

    )


def downgrade():
    op.drop_table("polls")

