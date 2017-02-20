"""empty message

Revision ID: 199cfbf3013b
Revises: None
Create Date: 2017-02-18 17:26:54.300216

"""

# revision identifiers, used by Alembic.
revision = '199cfbf3013b'
down_revision = None

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('address',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('modified_at', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('index', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('modified_at', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('description', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('country',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('modified_at', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('coordinates', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('coordinates'),
    sa.UniqueConstraint('name')
    )
    op.create_table('leed',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('modified_at', sa.DateTime(), nullable=True),
    sa.Column('email', sa.String(length=50), nullable=True),
    sa.Column('phone', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('phone')
    )
    op.create_table('message',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('modified_at', sa.DateTime(), nullable=True),
    sa.Column('subject', sa.String(length=256), nullable=False),
    sa.Column('content', sa.Text(), nullable=True),
    sa.Column('to', sa.Integer(), nullable=False),
    sa.Column('unread', sa.Boolean(), nullable=True),
    sa.Column('sent_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_message_to'), 'message', ['to'], unique=False)
    op.create_table('role',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('modified_at', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('status',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('modified_at', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('subcategory',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('modified_at', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('link', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('link'),
    sa.UniqueConstraint('name')
    )
    op.create_table('template',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('modified_at', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('html', sa.String(length=5000), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('html'),
    sa.UniqueConstraint('name')
    )
    op.create_table('type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('modified_at', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('modified_at', sa.DateTime(), nullable=True),
    sa.Column('first_name', sa.String(length=255), nullable=True),
    sa.Column('last_name', sa.String(length=255), nullable=True),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.Column('password', sa.String(length=255), nullable=True),
    sa.Column('avatar', sa.String(length=200), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.Column('confirmed_at', sa.DateTime(), nullable=True),
    sa.Column('last_login_at', sa.DateTime(), nullable=True),
    sa.Column('current_login_at', sa.DateTime(), nullable=True),
    sa.Column('last_login_ip', sa.String(length=55), nullable=True),
    sa.Column('current_login_ip', sa.String(length=55), nullable=True),
    sa.Column('login_count', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('city',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('modified_at', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('country', sa.Integer(), nullable=False),
    sa.Column('coordinates', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['country'], ['country.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('coordinates'),
    sa.UniqueConstraint('name')
    )
    op.create_table('notification',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('modified_at', sa.DateTime(), nullable=True),
    sa.Column('created_by', sa.Integer(), nullable=True),
    sa.Column('has_read', sa.Boolean(), nullable=True),
    sa.Column('action', sa.String(length=50), nullable=True),
    sa.Column('title', sa.String(length=50), nullable=True),
    sa.Column('message', sa.String(length=50), nullable=True),
    sa.ForeignKeyConstraint(['created_by'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('page',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('modified_at', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('link', sa.String(length=50), nullable=True),
    sa.Column('content', sa.String(length=500), nullable=True),
    sa.Column('template', sa.Integer(), nullable=True),
    sa.Column('category', sa.Integer(), nullable=True),
    sa.Column('subcategory', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['category'], ['category.id'], ),
    sa.ForeignKeyConstraint(['subcategory'], ['subcategory.id'], ),
    sa.ForeignKeyConstraint(['template'], ['template.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('link'),
    sa.UniqueConstraint('name')
    )
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('modified_at', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('description', sa.String(length=2500), nullable=True),
    sa.Column('property', sa.String(length=2500), nullable=True),
    sa.Column('article', sa.String(length=2500), nullable=True),
    sa.Column('price', sa.String(length=10), nullable=True),
    sa.Column('category', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['category'], ['category.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('roles_users',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['role.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], )
    )
    op.create_table('calculator',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('modified_at', sa.DateTime(), nullable=True),
    sa.Column('inout', sa.Boolean(), nullable=True),
    sa.Column('width_min', sa.String(length=50), nullable=True),
    sa.Column('width_max', sa.String(length=50), nullable=True),
    sa.Column('width_step', sa.String(length=50), nullable=True),
    sa.Column('width_start', sa.String(length=50), nullable=True),
    sa.Column('height_min', sa.String(length=50), nullable=True),
    sa.Column('height_max', sa.String(length=50), nullable=True),
    sa.Column('height_step', sa.String(length=50), nullable=True),
    sa.Column('height_start', sa.String(length=50), nullable=True),
    sa.Column('product', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['product'], ['product.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('image',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('modified_at', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('path', sa.Unicode(length=128), nullable=True),
    sa.Column('product', sa.Integer(), nullable=True),
    sa.Column('category', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['category'], ['category.id'], ),
    sa.ForeignKeyConstraint(['product'], ['product.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('organisation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('modified_at', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('address', sa.String(length=50), nullable=True),
    sa.Column('city', sa.Integer(), nullable=False),
    sa.Column('country', sa.Integer(), nullable=False),
    sa.Column('type', sa.Integer(), nullable=False),
    sa.Column('created_by', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['city'], ['city.id'], ),
    sa.ForeignKeyConstraint(['country'], ['country.id'], ),
    sa.ForeignKeyConstraint(['created_by'], ['user.id'], ),
    sa.ForeignKeyConstraint(['type'], ['type.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('size',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('modified_at', sa.DateTime(), nullable=True),
    sa.Column('price', sa.String(length=50), nullable=True),
    sa.Column('width', sa.String(length=50), nullable=True),
    sa.Column('height', sa.String(length=50), nullable=True),
    sa.Column('count', sa.String(length=50), nullable=True),
    sa.Column('type', sa.String(length=50), nullable=True),
    sa.Column('description', sa.String(length=2500), nullable=True),
    sa.Column('product', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['product'], ['product.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tag',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('modified_at', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('description', sa.String(length=2500), nullable=True),
    sa.Column('product', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['product'], ['product.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('contact',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('modified_at', sa.DateTime(), nullable=True),
    sa.Column('first_name', sa.String(length=50), nullable=False),
    sa.Column('last_name', sa.String(length=50), nullable=False),
    sa.Column('position', sa.String(length=50), nullable=False),
    sa.Column('email', sqlalchemy_utils.types.email.EmailType(length=255), nullable=False),
    sa.Column('phone_mobile', sa.String(length=50), nullable=False),
    sa.Column('phone_work', sa.String(length=50), nullable=True),
    sa.Column('phone_fax', sa.String(length=50), nullable=True),
    sa.Column('phone_other', sa.String(length=50), nullable=True),
    sa.Column('created_by', sa.Integer(), nullable=False),
    sa.Column('org_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['created_by'], ['user.id'], ),
    sa.ForeignKeyConstraint(['org_id'], ['organisation.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('phone_mobile')
    )
    op.create_table('tags_images',
    sa.Column('tags_ids', sa.Integer(), nullable=True),
    sa.Column('images_ids', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['images_ids'], ['image.id'], ),
    sa.ForeignKeyConstraint(['tags_ids'], ['tag.id'], )
    )
    op.create_table('project',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('modified_at', sa.DateTime(), nullable=True),
    sa.Column('start_date', sa.Date(), nullable=True),
    sa.Column('end_date', sa.Date(), nullable=True),
    sa.Column('status', sa.Integer(), nullable=True),
    sa.Column('created_by', sa.Integer(), nullable=True),
    sa.Column('org_id', sa.Integer(), nullable=True),
    sa.Column('contact_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['contact_id'], ['contact.id'], ),
    sa.ForeignKeyConstraint(['created_by'], ['user.id'], ),
    sa.ForeignKeyConstraint(['org_id'], ['organisation.id'], ),
    sa.ForeignKeyConstraint(['status'], ['status.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('activity',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('modified_at', sa.DateTime(), nullable=True),
    sa.Column('subject', sa.String(length=100), nullable=False),
    sa.Column('detail', sa.Text(), nullable=True),
    sa.Column('contact_id', sa.Integer(), nullable=True),
    sa.Column('org_id', sa.Integer(), nullable=True),
    sa.Column('project_id', sa.Integer(), nullable=True),
    sa.Column('created_by', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['contact_id'], ['contact.id'], ),
    sa.ForeignKeyConstraint(['created_by'], ['user.id'], ),
    sa.ForeignKeyConstraint(['org_id'], ['organisation.id'], ),
    sa.ForeignKeyConstraint(['project_id'], ['project.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('invoice',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('modified_at', sa.DateTime(), nullable=True),
    sa.Column('issue_date', sa.Date(), nullable=True),
    sa.Column('amount', sa.Integer(), nullable=False),
    sa.Column('paid', sa.Boolean(), nullable=True),
    sa.Column('created_by', sa.Integer(), nullable=True),
    sa.Column('project_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['created_by'], ['user.id'], ),
    sa.ForeignKeyConstraint(['project_id'], ['project.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('invoice')
    op.drop_table('activity')
    op.drop_table('project')
    op.drop_table('tags_images')
    op.drop_table('contact')
    op.drop_table('tag')
    op.drop_table('size')
    op.drop_table('organisation')
    op.drop_table('image')
    op.drop_table('calculator')
    op.drop_table('roles_users')
    op.drop_table('product')
    op.drop_table('page')
    op.drop_table('notification')
    op.drop_table('city')
    op.drop_table('user')
    op.drop_table('type')
    op.drop_table('template')
    op.drop_table('subcategory')
    op.drop_table('status')
    op.drop_table('role')
    op.drop_index(op.f('ix_message_to'), table_name='message')
    op.drop_table('message')
    op.drop_table('leed')
    op.drop_table('country')
    op.drop_table('category')
    op.drop_table('address')
    # ### end Alembic commands ###
