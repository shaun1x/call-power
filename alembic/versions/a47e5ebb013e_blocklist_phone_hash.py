"""blocklist_phone_hash

Revision ID: a47e5ebb013e
Revises: d1cbc9f7003c
Create Date: 2017-07-11 19:03:05.485924

"""

# revision identifiers, used by Alembic.
revision = 'a47e5ebb013e'
down_revision = 'd1cbc9f7003c'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('admin_blocklist', schema=None) as batch_op:
        batch_op.add_column(sa.Column('phone_hash', sa.String(length=64), nullable=True))

    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('admin_blocklist', schema=None) as batch_op:
        batch_op.drop_column('phone_hash')

    ### end Alembic commands ###
