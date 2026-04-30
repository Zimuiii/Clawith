"""add thinking_signature to chat_messages

Revision ID: 7e6a435b203a
Revises: add_file_activity_actions
Create Date: 2026-04-30 09:28:47.822099
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '7e6a435b203a'
down_revision: Union[str, None] = 'add_file_activity_actions'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('chat_messages', sa.Column('thinking_signature', sa.Text(), nullable=True))


def downgrade() -> None:
    op.drop_column('chat_messages', 'thinking_signature')
