import uuid

import aiohttp
from fastapi import HTTPException, status

from core.config import settings
from services.api.base import BaseAPIService


class EventAPIService(BaseAPIService):
    @classmethod
    async def get_list(cls) -> list[dict]:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                settings.api_line_provider_config.list_event_url
            ) as response:
                return await response.json()

    @classmethod
    async def get_detail_by_id(cls, id: uuid.UUID) -> dict:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                settings.api_line_provider_config.detail_event_url + "/" + str(id)
            ) as response:
                if response.status == status.HTTP_200_OK:
                    return await response.json()
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
