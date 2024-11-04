import logging

from fastapi import APIRouter, Body, Depends, HTTPException, Path, status

from api.v1.events.schemas import CreateEvent, Event, UpdateState
from common.schemas import BaseEsParams
from core.config import settings
from services.elastic.event import EventService, get_event_service
from services.producer.bet import BetRedisProducer, get_bet_producer

router = APIRouter()


@router.get("/events", response_model=list[Event], status_code=status.HTTP_200_OK)
async def list_event_view(event_service: EventService = Depends(get_event_service)):
    logging.info("::v1::get")
    res = await event_service.get_list(BaseEsParams())
    return [Event(**event_data) for event_data in res]


@router.post("/event", response_model=Event, status_code=status.HTTP_201_CREATED)
async def create_event_view(
    event: CreateEvent, event_service: EventService = Depends(get_event_service)
):
    logging.info("::v1::post")
    event_data = await event_service.create_detail(event.model_dump())
    return Event(**event_data)


@router.patch("/event/{event_id}", response_model=None, status_code=status.HTTP_200_OK)
async def update_event_state_view(
    new_state: UpdateState = Body(),
    event_id: str = Path(),
    bet_producer: BetRedisProducer = Depends(get_bet_producer),
    event_service: EventService = Depends(get_event_service),
):
    logging.info("::v1::patch")

    await event_service.update_detail(id=event_id, updated_data=new_state.model_dump())
    await bet_producer.bulk_update_bet_state(
        settings.update_bets_state_task_name, event_id, new_state.state
    )


@router.get("/event/{event_id}")
async def detail_event_view(
    event_id: str, event_service: EventService = Depends(get_event_service)
):
    logging.info("::v1::get")
    event_data = await event_service.get_detail(id=event_id)
    return Event(**event_data)
