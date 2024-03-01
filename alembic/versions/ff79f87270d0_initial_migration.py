"""Initial migration

Revision ID: ff79f87270d0
Revises: 
Create Date: 2024-02-27 19:49:20.856553

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'ff79f87270d0'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('books',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('title', sa.String(), nullable=True),
                    sa.Column('author', sa.String(), nullable=True),
                    sa.Column('year', sa.Integer(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_books_id'), 'books', ['id'], unique=False)
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=True),
                    sa.Column('first_name', sa.String(), nullable=True),
                    sa.Column('last_name', sa.String(), nullable=True),
                    sa.Column('password', sa.String(), nullable=True),
                    sa.Column('role', sa.Enum('customer', 'admin', 'librarian',
                                              name='user_role_enum'), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    op.create_table('user_books',
                    sa.Column('user_id', sa.Integer(), nullable=False),
                    sa.Column('book_id', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['book_id'], ['books.id'], ),
                    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
                    sa.PrimaryKeyConstraint('user_id', 'book_id')
                    )

    users_table = sa.sql.table(
        'users',
        sa.sql.column('email', sa.String),
        sa.sql.column('first_name', sa.String),
        sa.sql.column('last_name', sa.String),
        sa.sql.column('password', sa.String),
        sa.sql.column('role', sa.Enum('customer', 'admin', 'librarian', name='user_role_enum'))
    )

    op.bulk_insert(
        table=users_table,
        rows=[
            {'email': 'user1@example.com', 'first_name': 'John', 'last_name': 'Doe',
             'password': '$2b$12$Rit..Z9HQv4t3cL0KPlLXefwhShFow1m0Zgzaig5UWEazjPuqjv4G',
             'role': 'librarian'},
            {'email': 'user2@example.com', 'first_name': 'Jane', 'last_name': 'Doe',
             'password': '$2b$12$q0ir67lHNeU6ORhsPZzWteDrb/9WavXwW18VmvlFgcjZFUA5Vx3vu',
             'role': 'admin'},
            {'email': 'user3@example.com', 'first_name': 'Jim', 'last_name': 'Doe',
             'password': '$2b$12$7hHAK0IW58luSRmY6C2WEuAQLS9VBl8NX1C8eEyp8a.usW4umFyKy',
             'role': 'customer'}
        ]
    )


def downgrade() -> None:
    op.drop_table('user_books')
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_books_id'), table_name='books')
    op.drop_table('books')
