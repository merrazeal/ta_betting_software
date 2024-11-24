import asyncio
import logging
from contextlib import asynccontextmanager
from logging import config as logging_config
from typing import AsyncIterator

import asyncpg
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from api.v1.bets import routes as bet_routes
from api.v1.events import routes as event_routes
from core.config import settings
from core.logger import LOGGING
from db.postgres.factory import postgres
from db.postgres.setup import init_db
from services.pubsub.consumer import AsyncConsumer
from services.pubsub.executor import AsyncTaskExecutor
from services.pubsub.subscribers import AsyncRedisSubscriber


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    await init_db()  # meh
    postgres["pool"] = await asyncpg.create_pool(
        user=settings.postgres_config.username,
        password=settings.postgres_config.password,
        database=settings.postgres_config.database_name,
        host=settings.postgres_config.host,
        port=settings.postgres_config.port,
        min_size=10,
        max_size=40,
    )
    bet_async_consumer = AsyncConsumer(
        subscriber=AsyncRedisSubscriber(
            channel_name="bets_channel", logger=logging.getLogger("consumer")
        ),
        task_executor=AsyncTaskExecutor(
            task_registry={
                "update_bets_state": "services.pubsub.tasks.bets",
            },
            exe_queue=asyncio.Queue(),
            logger=logging.getLogger("executor"),
        ),
        logger=logging.getLogger("consumer"),
    )
    await bet_async_consumer.consume()
    yield
    await postgres["pool"].close()
    await bet_async_consumer.close()


def get_application() -> FastAPI:
    logging_config.dictConfig(LOGGING)
    _app = FastAPI(
        title=settings.project_name,
        default_response_class=ORJSONResponse,
        lifespan=lifespan,
        docs_url="/api/openapi/",
        openapi_url="/api/openapi/api.json",
    )
    _app.include_router(bet_routes.router, prefix="/api/v1")
    _app.include_router(event_routes.router, prefix="/api/v1")
    return _app


app = get_application()
