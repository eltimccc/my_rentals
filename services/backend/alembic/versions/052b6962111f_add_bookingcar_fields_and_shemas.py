"""add BookingCar fields and shemas

Revision ID: 052b6962111f
Revises: e7cbd621d3ef
Create Date: 2023-09-15 19:09:59.166032

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "052b6962111f"
down_revision: Union[str, None] = "e7cbd621d3ef"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("bookingcar", sa.Column("first_name", sa.String(), nullable=True))
    op.add_column("bookingcar", sa.Column("last_name", sa.String(), nullable=True))
    op.add_column("bookingcar", sa.Column("phone", sa.String(), nullable=True))
    op.add_column("bookingcar", sa.Column("email", sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("bookingcar", "email")
    op.drop_column("bookingcar", "phone")
    op.drop_column("bookingcar", "last_name")
    op.drop_column("bookingcar", "first_name")
    # ### end Alembic commands ###
