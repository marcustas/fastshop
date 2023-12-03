"""empty message

Revision ID: 40f8af84ecb8
Revises: 3b3e7aef66e3
Create Date: 2023-12-03 13:16:03.296231

"""
from typing import (
    Sequence,
    Union,
)

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = '40f8af84ecb8'
down_revision: Union[str, None] = '3b3e7aef66e3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_addresses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('city', sa.String(), nullable=True),
    sa.Column('street', sa.String(), nullable=True),
    sa.Column('house', sa.String(), nullable=True),
    sa.Column('apartment', sa.String(), nullable=True),
    sa.Column('post_code', sa.String(), nullable=True),
    sa.Column('floor', sa.String(), nullable=True),
    sa.Column('additional_info', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_addresses_id'), 'user_addresses', ['id'], unique=False)
    op.add_column('users', sa.Column('date_joined', sa.DateTime(), nullable=True))
    op.add_column('users', sa.Column('last_login', sa.DateTime(), nullable=True))
    op.add_column('users', sa.Column('is_temporary', sa.Boolean(), nullable=True))
    op.drop_index('ix_users_username', table_name='users')
    op.drop_column('users', 'username')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('username', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.create_index('ix_users_username', 'users', ['username'], unique=False)
    op.drop_column('users', 'is_temporary')
    op.drop_column('users', 'last_login')
    op.drop_column('users', 'date_joined')
    op.drop_index(op.f('ix_user_addresses_id'), table_name='user_addresses')
    op.drop_table('user_addresses')
    # ### end Alembic commands ###
