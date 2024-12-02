"""empty message

Revision ID: 2c3d9dc9ba07
Revises: 4f756c62b7e7
Create Date: 2024-12-02 00:58:15.058896

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2c3d9dc9ba07'
down_revision = '4f756c62b7e7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('amico',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('part_number', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('part_number')
    )
    op.create_table('kenall_accessories',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('doorframe', sa.String(), nullable=False),
    sa.Column('amico_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['amico_id'], ['amico.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('kenall_diffuser',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('diffuser', sa.String(), nullable=False),
    sa.Column('amico_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['amico_id'], ['amico.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('kenall_doorframe',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('doorframe', sa.String(), nullable=False),
    sa.Column('amico_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['amico_id'], ['amico.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('kenall_driver',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('driver', sa.String(), nullable=False),
    sa.Column('amico_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['amico_id'], ['amico.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('kenall_lamp',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('lamp', sa.String(), nullable=False),
    sa.Column('amico_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['amico_id'], ['amico.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('kenall_model',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('model', sa.String(), nullable=False),
    sa.Column('amico_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['amico_id'], ['amico.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('kenall_mounting',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('mounting', sa.String(), nullable=False),
    sa.Column('amico_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['amico_id'], ['amico.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('kenall_options',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('doorframe', sa.String(), nullable=False),
    sa.Column('amico_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['amico_id'], ['amico.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('kenall_voltage',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('voltage', sa.String(), nullable=False),
    sa.Column('amico_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['amico_id'], ['amico.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('part_number')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('part_number',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_part', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('amico_part', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='part_number_pkey')
    )
    op.drop_table('kenall_voltage')
    op.drop_table('kenall_options')
    op.drop_table('kenall_mounting')
    op.drop_table('kenall_model')
    op.drop_table('kenall_lamp')
    op.drop_table('kenall_driver')
    op.drop_table('kenall_doorframe')
    op.drop_table('kenall_diffuser')
    op.drop_table('kenall_accessories')
    op.drop_table('amico')
    # ### end Alembic commands ###