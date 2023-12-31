"""add contact model

Revision ID: bd9237ff73d5
Revises: 956cafc45468
Create Date: 2023-08-31 17:45:25.527746

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "bd9237ff73d5"
down_revision: Union[str, None] = "956cafc45468"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "contact",
        sa.Column(
            "id", sa.Integer(), nullable=False, primary_key=True, autoincrement=True
        ),
        sa.Column("email", sa.String(length=50), nullable=True),
        sa.Column("phone", sa.String(length=50), nullable=True),
        sa.Column("phone2", sa.String(length=50), nullable=True),
        sa.Column("vk", sa.String(length=50), nullable=True),
        sa.Column("address", sa.String(length=50), nullable=True),
        sa.Column("description", sa.String(length=50), nullable=True),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("contact")
    # ### end Alembic commands ###
