"""add News model only

Revision ID: bc3a432527d5
Revises: a35c5b87aa52
Create Date: 2023-09-09 20:28:26.040250

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "bc3a432527d5"
down_revision: Union[str, None] = "a35c5b87aa52"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "news",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(), nullable=True),
        sa.Column("content", sa.String(), nullable=True),
        sa.Column("author", sa.String(), nullable=True),
        sa.Column("publication_date", sa.DateTime(), nullable=True),
        sa.Column("photo_url", sa.String(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_news_id"), "news", ["id"], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_news_id"), table_name="news")
    op.drop_table("news")
    # ### end Alembic commands ###