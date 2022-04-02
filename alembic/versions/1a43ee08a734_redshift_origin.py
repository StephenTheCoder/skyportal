"""Redshift origin

Revision ID: 1a43ee08a734
Revises: 5df4b399aae2
Create Date: 2022-03-22 23:53:32.815303

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1a43ee08a734'
down_revision = '5df4b399aae2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('objs', sa.Column('redshift_origin', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('objs', 'redshift_origin')
    # ### end Alembic commands ###