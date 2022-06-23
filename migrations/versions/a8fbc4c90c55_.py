"""empty message

Revision ID: a8fbc4c90c55
Revises: 4a77fe8b6501
Create Date: 2022-06-22 22:52:58.350127

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a8fbc4c90c55'
down_revision = '4a77fe8b6501'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'last_name',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
    op.alter_column('user', 'numero_telefonico',
               existing_type=sa.VARCHAR(length=25),
               nullable=True)
    op.alter_column('user', 'numero_fpv',
               existing_type=sa.VARCHAR(length=25),
               nullable=True)
    op.alter_column('user', 'area_de_especialidad',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
    op.alter_column('user', 'pais',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
    op.alter_column('user', 'ciudad',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
    op.alter_column('user', 'status',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'status',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    op.alter_column('user', 'ciudad',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
    op.alter_column('user', 'pais',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
    op.alter_column('user', 'area_de_especialidad',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
    op.alter_column('user', 'numero_fpv',
               existing_type=sa.VARCHAR(length=25),
               nullable=False)
    op.alter_column('user', 'numero_telefonico',
               existing_type=sa.VARCHAR(length=25),
               nullable=False)
    op.alter_column('user', 'last_name',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
    # ### end Alembic commands ###
