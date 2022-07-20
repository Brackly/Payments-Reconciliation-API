"""init

Revision ID: bd4fa4526176
Revises: 
Create Date: 2022-07-20 16:56:45.948643

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bd4fa4526176'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'payments',
        sa.Column('TransactionType',sa.String,nullable=False),
        sa.Column('TransID',sa.String, primary_key=True),
        sa.Column('TransTime',sa.String,nullable=False),
        sa.Column('TransAmount',sa.String,nullable=False),
        sa.Column('BusinessShortCode',sa.String,nullable=False),
        sa.Column('BillRefNumber',sa.String,nullable=False),
        sa.Column('InvoiceNumber',sa.String,nullable=True),
        sa.Column('OrgAccountBalance',sa.String,nullable=True),
        sa.Column('ThirdPartyTransID',sa.String,nullable=True),
        sa.Column('MSISDN',sa.String,nullable=False),
        sa.Column('FirstName',sa.String,nullable=False),
        sa.Column('seen',sa.Boolean,default=False)
    )
    


def downgrade() -> None:
    op.drop_table('payments')
