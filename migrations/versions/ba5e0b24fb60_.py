"""empty message

Revision ID: ba5e0b24fb60
Revises: 9d3493d4f28c
Create Date: 2022-03-10 00:31:31.554911

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ba5e0b24fb60'
down_revision = '9d3493d4f28c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('search',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('result', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('search')
    # ### end Alembic commands ###
