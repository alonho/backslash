"""user preferences

Revision ID: bd2b2746e4ed
Revises: c9193bcb6894
Create Date: 2016-06-21 09:18:37.621720

"""

# revision identifiers, used by Alembic.
revision = 'bd2b2746e4ed'
down_revision = 'c9193bcb6894'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_preference',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('preference', sa.String(length=256), nullable=False),
    sa.Column('value', postgresql.JSONB(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('user_id', 'preference')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_preference')
    ### end Alembic commands ###