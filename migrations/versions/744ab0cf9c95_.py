"""empty message

Revision ID: 744ab0cf9c95
Revises: 
Create Date: 2022-04-05 22:42:16.708502

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '744ab0cf9c95'
down_revision = None
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
