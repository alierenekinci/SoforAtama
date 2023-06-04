"""empty message

Revision ID: 422061dd8805
Revises: 9ea2b011098e
Create Date: 2023-06-04 14:10:16.310428

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '422061dd8805'
down_revision = '9ea2b011098e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('otobus', schema=None) as batch_op:
        batch_op.add_column(sa.Column('otobus_plaka', sa.String(length=150), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('otobus', schema=None) as batch_op:
        batch_op.drop_column('otobus_plaka')

    # ### end Alembic commands ###
