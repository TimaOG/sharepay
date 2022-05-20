"""twst

Revision ID: c4f907bbc276
Revises: 322f22962583
Create Date: 2022-04-06 20:22:30.124827

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c4f907bbc276'
down_revision = '322f22962583'
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
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('fundName')
    )
    op.create_table('users',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('email', sa.VARCHAR(length=50), nullable=True),
    sa.Column('password', sa.VARCHAR(length=500), nullable=False),
    sa.Column('isAdmin', sa.BOOLEAN(), nullable=True),
    sa.Column('trustFunds', sa.BLOB(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###
