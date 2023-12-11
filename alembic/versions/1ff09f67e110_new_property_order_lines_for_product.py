"""new property order_lines for Product

Revision ID: 1ff09f67e110
Revises: d68ea522b645
Create Date: 2023-12-11 10:46:41.176305

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1ff09f67e110'
down_revision: Union[str, None] = 'd68ea522b645'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
