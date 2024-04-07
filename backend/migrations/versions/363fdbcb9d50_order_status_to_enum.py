"""order status to enum

Revision ID: 363fdbcb9d50
Revises: 019bc261d7eb
Create Date: 2024-03-17 23:00:20.903656

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '363fdbcb9d50'
down_revision: Union[str, None] = '019bc261d7eb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('order',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('date_creation', sa.Date(), nullable=True),
    sa.Column('date_ending', sa.Date(), nullable=True),
    sa.Column('start_location', sa.String(), nullable=True),
    sa.Column('finish_location', sa.String(), nullable=True),
    sa.Column('driver_id', sa.Integer(), nullable=True),
    sa.Column('customer_id', sa.Integer(), nullable=True),
    sa.Column('car_id', sa.Integer(), nullable=True),
    sa.Column('volume', sa.Float(), nullable=True),
    sa.Column('weight', sa.Float(), nullable=True),
    sa.Column('status', sa.Enum('new', 'in_progress', 'done', name='orderstatus'), nullable=True),
    sa.Column('customer_estimation_id', sa.Integer(), nullable=True),
    sa.Column('driver_estimation_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['car_id'], ['car.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['customer_estimation_id'], ['customer_estimation.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['customer_id'], ['customer.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['driver_estimation_id'], ['driver_estimation.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['driver_id'], ['driver.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('order')
    # ### end Alembic commands ###