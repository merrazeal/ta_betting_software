import uuid
from functools import lru_cache

from elasticsearch import AsyncElasticsearch, NotFoundError
from fastapi import Depends, HTTPException, status

from common.schemas import BaseEsParams
from core.config import settings
from db.elastic.factory import get_elastic
from services.elastic.mixin import ListMixinEsService
from services.elastic.query_builder import EsSearchQueryConstuctor


class EventService(ListMixinEsService):
    def __init__(self, elastic: AsyncElasticsearch, constructor) -> None:
        self.elastic = elastic
        self.es_search_constructor = constructor

    async def get_detail(self, id: uuid.UUID) -> dict:
        try:
            doc = await self.elastic.get(index=settings.event_index, id=str(id))
        except NotFoundError:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return doc["_source"]

    async def get_list(self, params: BaseEsParams) -> list[dict]:
        query = self.get_list_query(params)
        response = await self.elastic.search(index=settings.event_index, body=query)
        return [hit["_source"] for hit in response["hits"]["hits"]]

    async def update_detail(self, id: uuid.UUID, updated_data: dict) -> None:
        try:
            await self.elastic.update(
                index=settings.event_index, id=str(id), body={"doc": updated_data}
            )
        except NotFoundError:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    async def create_detail(self, event_data: dict) -> dict:
        new_uuid = str(uuid.uuid4())
        event_data["id"] = new_uuid
        await self.elastic.index(
            index=settings.event_index,
            id=new_uuid,
            body=event_data,
        )
        return event_data


@lru_cache()
def get_event_service(
    elastic: AsyncElasticsearch = Depends(get_elastic),
) -> EventService:
    return EventService(elastic=elastic, constructor=EsSearchQueryConstuctor())
