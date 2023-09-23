"""Add fields for additional services

Revision ID: 0a88970c19c3
Revises: 67bba9a4c829
Create Date: 2023-09-23 17:14:14.302173

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0a88970c19c3'
down_revision: Union[str, None] = '67bba9a4c829'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('bookingcar', sa.Column('additional_services_airport', sa.Boolean(), nullable=True))
    op.add_column('bookingcar', sa.Column('additional_services_railway_station', sa.Boolean(), nullable=True))
    op.add_column('bookingcar', sa.Column('additional_services_your_address', sa.Boolean(), nullable=True))
    op.add_column('bookingcar', sa.Column('additional_services_add_driver', sa.Boolean(), nullable=True))
    op.add_column('bookingcar', sa.Column('additional_services_washing', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('bookingcar', 'additional_services_washing')
    op.drop_column('bookingcar', 'additional_services_add_driver')
    op.drop_column('bookingcar', 'additional_services_your_address')
    op.drop_column('bookingcar', 'additional_services_railway_station')
    op.drop_column('bookingcar', 'additional_services_airport')
    # ### end Alembic commands ###