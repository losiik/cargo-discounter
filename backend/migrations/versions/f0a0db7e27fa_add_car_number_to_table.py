"""add car number to table

Revision ID: f0a0db7e27fa
Revises: bf5b6d92dc39
Create Date: 2024-03-14 22:25:20.191663

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f0a0db7e27fa'
down_revision: Union[str, None] = 'bf5b6d92dc39'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('car', sa.Column('car_number', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('car', 'car_number')
    # ### end Alembic commands ###
