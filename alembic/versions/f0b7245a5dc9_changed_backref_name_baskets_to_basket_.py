"""changed backref name basketS to basket in Basket.user

Revision ID: f0b7245a5dc9
Revises: 1ff09f67e110
Create Date: 2023-12-11 11:02:42.965263

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f0b7245a5dc9'
down_revision: Union[str, None] = '1ff09f67e110'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
