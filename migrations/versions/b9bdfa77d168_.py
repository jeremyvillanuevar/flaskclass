"""empty message

Revision ID: b9bdfa77d168
Revises: 
Create Date: 2024-02-24 22:38:48.163417

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b9bdfa77d168'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.add_column(sa.Column('date_posted', sa.DateTime(), nullable=False))
        batch_op.alter_column('content',
               existing_type=sa.VARCHAR(length=500),
               type_=sa.String(length=300),
               existing_nullable=True)
        batch_op.alter_column('post_img',
               existing_type=sa.VARCHAR(length=200),
               type_=sa.String(length=300),
               existing_nullable=True)
        batch_op.create_foreign_key(batch_op.f('fk_post_user_id_user'), 'user', ['user_id'], ['id'])

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password', sa.String(length=120), nullable=False))
        batch_op.alter_column('username',
               existing_type=sa.VARCHAR(length=80),
               nullable=False)
        batch_op.alter_column('email',
               existing_type=sa.VARCHAR(length=80),
               type_=sa.String(length=120),
               nullable=False)
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(length=80),
               type_=sa.String(length=120),
               existing_nullable=False)
        batch_op.create_unique_constraint(batch_op.f('uq_user_email'), ['email'])
        batch_op.create_unique_constraint(batch_op.f('uq_user_username'), ['username'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('uq_user_username'), type_='unique')
        batch_op.drop_constraint(batch_op.f('uq_user_email'), type_='unique')
        batch_op.alter_column('name',
               existing_type=sa.String(length=120),
               type_=sa.VARCHAR(length=80),
               existing_nullable=False)
        batch_op.alter_column('email',
               existing_type=sa.String(length=120),
               type_=sa.VARCHAR(length=80),
               nullable=True)
        batch_op.alter_column('username',
               existing_type=sa.VARCHAR(length=80),
               nullable=True)
        batch_op.drop_column('password')

    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_post_user_id_user'), type_='foreignkey')
        batch_op.alter_column('post_img',
               existing_type=sa.String(length=300),
               type_=sa.VARCHAR(length=200),
               existing_nullable=True)
        batch_op.alter_column('content',
               existing_type=sa.String(length=300),
               type_=sa.VARCHAR(length=500),
               existing_nullable=True)
        batch_op.drop_column('date_posted')

    # ### end Alembic commands ###
