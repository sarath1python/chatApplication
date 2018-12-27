"""first migration

Revision ID: 623d6b40c853
Revises: 
Create Date: 2018-12-26 12:31:09.727020

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '623d6b40c853'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=40), nullable=True),
    sa.Column('user_name', sa.String(length=50), nullable=True),
    sa.Column('password', sa.String(length=120), nullable=True),
    sa.Column('last_login', sa.DateTime(), nullable=True),
    sa.Column('created_date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('token',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('token', sa.String(length=40), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('token')
    op.drop_table('user')
    # ### end Alembic commands ###