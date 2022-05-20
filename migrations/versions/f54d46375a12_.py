"""empty message

Revision ID: f54d46375a12
Revises: 2ba11600f176
Create Date: 2022-04-10 10:59:54.573907

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f54d46375a12'
down_revision = '2ba11600f176'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('fund')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('fund',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('fundName', sa.VARCHAR(length=50), nullable=True),
    sa.Column('fundDiscrib', sa.TEXT(), nullable=True),
    sa.Column('fundLink', sa.VARCHAR(length=500), nullable=True),
    sa.Column('fundImageLink', sa.VARCHAR(length=500), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('fundName')
    )
    op.create_table('users',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=100), nullable=True),
    sa.Column('email', sa.VARCHAR(length=100), nullable=True),
    sa.Column('password', sa.VARCHAR(length=500), nullable=False),
    sa.Column('isAdmin', sa.BOOLEAN(), nullable=True),
    sa.Column('trustFunds', sa.BLOB(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###