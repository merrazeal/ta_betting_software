from contextlib import asynccontextmanager

import asyncpg

from core.config import settings


@asynccontextmanager
async def get_connection():
    connection = await asyncpg.connect(
        user=settings.postgres_config.username,
        password=settings.postgres_config.password,
        database=settings.postgres_config.database_name,
        host=settings.postgres_config.host,
        port=settings.postgres_config.port,
    )
    try:
        yield connection
    finally:
        await connection.close()
