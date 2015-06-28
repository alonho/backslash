"""empty message

Revision ID: 4de4cbc0ba5
Revises: 1a416935ea4
Create Date: 2015-06-27 23:00:58.035276

"""

# revision identifiers, used by Alembic.
revision = '4de4cbc0ba5'
down_revision = '1a416935ea4'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=256), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('subject',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=256), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('product_version',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('version', sa.String(length=256), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('product_id', 'version')
    )
    op.create_index(op.f('ix_product_version_product_id'), 'product_version', ['product_id'], unique=False)
    op.create_table('product_revision',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('product_version_id', sa.Integer(), nullable=False),
    sa.Column('revision', sa.String(length=256), nullable=True),
    sa.ForeignKeyConstraint(['product_version_id'], ['product_version.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('product_version_id', 'revision')
    )
    op.create_index(op.f('ix_product_revision_product_version_id'), 'product_revision', ['product_version_id'], unique=False)
    op.create_table('subject_instance',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('subject_id', sa.Integer(), nullable=False),
    sa.Column('revision_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['revision_id'], ['product_revision.id'], ),
    sa.ForeignKeyConstraint(['subject_id'], ['subject.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_subject_instance_revision_id'), 'subject_instance', ['revision_id'], unique=False)
    op.create_index(op.f('ix_subject_instance_subject_id'), 'subject_instance', ['subject_id'], unique=False)
    op.create_table('session_subject',
    sa.Column('session_id', sa.Integer(), nullable=True),
    sa.Column('subject_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['session_id'], ['session.id'], ),
    sa.ForeignKeyConstraint(['subject_id'], ['subject_instance.id'], )
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('session_subject')
    op.drop_index(op.f('ix_subject_instance_subject_id'), table_name='subject_instance')
    op.drop_index(op.f('ix_subject_instance_revision_id'), table_name='subject_instance')
    op.drop_table('subject_instance')
    op.drop_index(op.f('ix_product_revision_product_version_id'), table_name='product_revision')
    op.drop_table('product_revision')
    op.drop_index(op.f('ix_product_version_product_id'), table_name='product_version')
    op.drop_table('product_version')
    op.drop_table('subject')
    op.drop_table('product')
    ### end Alembic commands ###