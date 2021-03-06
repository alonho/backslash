"""Convert errors to text

Revision ID: 315e71d436e
Revises: 37bc6a190f
Create Date: 2015-10-25 14:20:47.813675

"""

# revision identifiers, used by Alembic.
revision = '315e71d436e'
down_revision = '37bc6a190f'

from alembic import op


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.execute('ALTER TABLE error ALTER COLUMN message TYPE text;')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.execute('ALTER TABLE error ALTER COLUMN message TYPE varchar(256);')
    ### end Alembic commands ###
