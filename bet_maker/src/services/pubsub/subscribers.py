import json
import logging

from redis.asyncio import StrictRedis

from core.config import settings
from services.pubsub.ports.subsciber import BaseAsyncSubscriber
from services.pubsub.message import Message


class AsyncRedisSubscriber(BaseAsyncSubscriber):

    def __init__(self, channel_name: str, logger: logging.Logger = logging.getLogger("")) -> None:
        self.client = StrictRedis(
            host=settings.redis_pubsub_config.host,
            port=settings.redis_pubsub_config.port,
            db=settings.redis_pubsub_config.db,
        )
        self.channel = self.client.pubsub()
        self.channel_name = channel_name
        self.logger = logger

    async def initialize(self) -> None:
        await self.channel.subscribe(self.channel_name)

    async def receive(self) -> Message | None:
        raw_message = await self.channel.get_message(ignore_subscribe_messages=True)
        if raw_message:
            return Message(**json.loads(raw_message["data"].decode("utf-8")))

    async def close(self) -> None:
        await self.channel.close()
        await self.client.close()
