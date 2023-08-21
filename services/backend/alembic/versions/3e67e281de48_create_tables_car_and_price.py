from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '3e67e281de48'
down_revision: Union[str, None] = '0435282b788f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'prices',
        sa.Column('id', sa.Integer(), primary_key=True, index=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('one_day', sa.Integer(), nullable=False),
        sa.Column('two_three_days', sa.Integer(), nullable=False),
        sa.Column('four_seven_days', sa.Integer(), nullable=False),
        sa.Column('eight_fourteen_days', sa.Integer(), nullable=False),
        sa.Column('fifteen_thirty_days', sa.Integer(), nullable=False),
        sa.Column('weekend', sa.Integer(), nullable=False),
        sa.Column('deposit', sa.Integer(), nullable=False),
    )

    op.create_table(
        'cars',
        sa.Column('id', sa.Integer(), primary_key=True, index=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('price_id', sa.Integer(), sa.ForeignKey('prices.id')),
        sa.Column('photo_url', sa.String(), nullable=True),
        sa.Column('description', sa.Text(), nullable=True),
        sa.Column('base_price', sa.Integer(), nullable=True),
        sa.Column('color', sa.String(50), nullable=True),
        sa.Column('transmission', sa.String(50), nullable=True),
        sa.Column('air_cold', sa.String(50), nullable=True),
        sa.Column('power', sa.Integer(), nullable=True),
        sa.Column('fuel_type', sa.String(50), nullable=True),
        sa.Column('fuel_rate', sa.String(50), nullable=True),
        sa.Column('year', sa.Integer(), nullable=True),
    )


def downgrade() -> None:
    op.drop_table('cars')
    op.drop_table('prices')
