"""empty message

Revision ID: 4a0850528d29
Revises: be95eb2f9305
Create Date: 2020-05-28 01:40:01.481906

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4a0850528d29'
down_revision = 'be95eb2f9305'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_post_body', table_name='post')
    op.create_index(op.f('ix_post_body'), 'post', ['body'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_post_body'), table_name='post')
    op.create_index('ix_post_body', 'post', ['body'], unique=1)
    # ### end Alembic commands ###
