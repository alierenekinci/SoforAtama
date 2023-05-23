"""empty message

Revision ID: 0301cd400cfe
Revises: 254d82b0a0b2
Create Date: 2023-05-18 16:13:34.142182

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0301cd400cfe'
down_revision = '254d82b0a0b2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('otobus', schema=None) as batch_op:
        batch_op.add_column(sa.Column('otobus_sayi', sa.BigInteger(), nullable=True))
        batch_op.drop_column('otobus_sayı')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('otobus', schema=None) as batch_op:
        batch_op.add_column(sa.Column('otobus_sayı', sa.BIGINT(), autoincrement=False, nullable=True))
        batch_op.drop_column('otobus_sayi')

    # ### end Alembic commands ###