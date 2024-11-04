import logging

from db.postgres.conn import get_connection
from db.postgres.queries import get_update_bet_state_query

logger = logging.getLogger("consumer")


async def update_bets_state(event_id: str, state: int) -> None:
    async with get_connection() as connection:
        await connection.execute(get_update_bet_state_query(), state, event_id)
