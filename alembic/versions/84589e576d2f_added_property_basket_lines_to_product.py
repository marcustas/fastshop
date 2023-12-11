"""added property basket_lines to Product

Revision ID: 84589e576d2f
Revises: f0b7245a5dc9
Create Date: 2023-12-11 11:07:10.598295

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '84589e576d2f'
down_revision: Union[str, None] = 'f0b7245a5dc9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
