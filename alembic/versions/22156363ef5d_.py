"""empty message

Revision ID: 22156363ef5d
Revises: 
Create Date: 2016-03-14 13:09:03.962303

"""

# revision identifiers, used by Alembic.
revision = '22156363ef5d'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('inpatientepisode', sa.Column('admission_diagnosis', sa.String(length=250), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('inpatientepisode', 'admission_diagnosis')
    ### end Alembic commands ###