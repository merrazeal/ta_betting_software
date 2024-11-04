from db.postgres.conn import get_connection
from db.postgres.queries import create_bets_table_query


async def init_db():
    async with get_connection() as connection:
        await connection.execute(create_bets_table_query())
