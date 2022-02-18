"""create_user_table

Revision ID: 59f1b4b04607
Revises: 
Create Date: 2022-02-15 14:38:03.289841

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '59f1b4b04607'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
    'users',
    sa.Column('id', sa.Integer()),
    sa.Column('username', sa.String(length=30), nullable=False),
    sa.Column('email', sa.VARCHAR(200), nullable=False),
    )
   

def downgrade():
    op.drop_table("users")

