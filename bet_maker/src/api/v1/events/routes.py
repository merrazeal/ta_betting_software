import logging

from fastapi import APIRouter, status

from api.v1.events.schemas import Event
from services.api.event import EventAPIService

router = APIRouter()


@router.get("/events", response_model=list[Event], status_code=status.HTTP_200_OK)
async def list_event_view():
    logging.info("::v1::get")
    res = await EventAPIService.get_list()
    return [Event(**event) for event in res]
