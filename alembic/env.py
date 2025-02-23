from sqlalchemy import engine_from_config, pool
from sqlalchemy.ext.asyncio import create_async_engine
from alembic import context
import os

config = context.config

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+asyncpg://postgres:postgres@localhost:5432/postgres")

def run_migrations_online():
    connectable = create_async_engine(DATABASE_URL, poolclass=pool.NullPool)

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=None)
        with context.begin_transaction():
            context.run_migrations()
