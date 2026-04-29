"""Add agent_file_sent and agent_file_received to activity_action_enum

Revision ID: add_file_activity_actions
Revises: rm_agent_credential_secrets
Create Date: 2026-04-29
"""
from alembic import op
import sqlalchemy as sa

# revision identifiers
revision = 'add_file_activity_actions'
down_revision = 'rm_agent_credential_secrets'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Add new enum values to activity_action_enum
    op.execute("ALTER TYPE activity_action_enum ADD VALUE IF NOT EXISTS 'agent_file_sent'")
    op.execute("ALTER TYPE activity_action_enum ADD VALUE IF NOT EXISTS 'agent_file_received'")


def downgrade() -> None:
    # PostgreSQL doesn't support removing enum values directly
    # Would need to recreate the enum type, which is complex
    pass
