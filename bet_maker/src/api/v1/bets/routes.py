import logging
import time

from asyncpg import Pool
from fastapi import APIRouter, Depends, HTTPException, status

from api.v1.bets.schemas import Bet, CreateBet
from db.postgres.factory import get_pool
from db.postgres.queries import get_all_bets_query, get_insert_bet_query
from services.api.event import EventAPIService

router = APIRouter()


@router.get("/bets", response_model=list[Bet], status_code=status.HTTP_200_OK)
async def list_bet_view(pool: Pool = Depends(get_pool)):
    logging.info("::v1::get")
    async with pool.acquire() as connection:  # TODO db service
        tuples = await connection.fetch(get_all_bets_query())
        bets = [Bet(id=tuple["id"], state=tuple["state"]) for tuple in tuples]
    return bets


@router.post("/bet", response_model=Bet, status_code=status.HTTP_201_CREATED)
async def create_bet_view(bet: CreateBet, pool: Pool = Depends(get_pool)):
    logging.info("::v1::post")
    event = await EventAPIService.get_detail_by_id(bet.event_id)
    if deadline := event.get("deadline", None):
        if deadline > time.time():
            async with pool.acquire() as connection:
                bet_id = await connection.fetchval(
                    get_insert_bet_query(),
                    bet.event_id,
                    bet.amount,
                )
            return Bet(id=bet_id)
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
