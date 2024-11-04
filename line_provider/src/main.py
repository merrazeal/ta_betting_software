from contextlib import asynccontextmanager
from logging import config as logging_config
from typing import AsyncIterator

from elasticsearch import AsyncElasticsearch
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from redis.asyncio import StrictRedis

from api.v1.events.routers import router as event_router
from core.config import settings
from core.logger import LOGGING
from db.elastic.factory import elastic
from db.redis.factory import redis


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    redis["client"] = StrictRedis(
        host=settings.redis_pubsub_config.host,
        port=settings.redis_pubsub_config.port,
        db=settings.redis_pubsub_config.db,
    )
    elastic["client"] = AsyncElasticsearch(hosts=[str(settings.elastic_url)])
    yield
    await redis["client"].close()
    await elastic["client"].close()


def get_application() -> FastAPI:
    logging_config.dictConfig(LOGGING)
    _app = FastAPI(
        default_response_class=ORJSONResponse,
        lifespan=lifespan,
        docs_url="/api/openapi/",
        openapi_url="/api/openapi/api.json",
    )
    _app.include_router(event_router, prefix="/api/v1")
    return _app


app = get_application()
