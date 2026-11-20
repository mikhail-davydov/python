"""Add reviews table and product rating

Revision ID: a1b2c3d4e5f6
Revises: 6bf554303bb8
Create Date: 2026-11-21 12:00:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a1b2c3d4e5f6'
down_revision: Union[str, None] = '6bf554303bb8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Создаём таблицу reviews
    op.create_table('reviews',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('comment', sa.Text(), nullable=True),
    sa.Column('comment_date', sa.DateTime(), server_default=sa.text('now()')),
    sa.Column('grade', sa.Integer(), nullable=False),
    sa.Column('is_active', sa.Boolean(), server_default=sa.text('true')),
    sa.CheckConstraint('grade >= 1 AND grade <= 5', name='check_grade_range'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id']),
    sa.ForeignKeyConstraint(['product_id'], ['products.id']),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_reviews_product_id'), 'reviews', ['product_id'], unique=False)

    # Добавляем столбец rating в products
    op.add_column('products', sa.Column('rating', sa.Float(), nullable=True, server_default=sa.text('0')))


def downgrade() -> None:
    op.drop_column('products', 'rating')
    op.drop_index(op.f('ix_reviews_product_id'), table_name='reviews')
    op.drop_table('reviews')
