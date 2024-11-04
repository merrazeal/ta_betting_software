from functools import lru_cache

import backoff
from fastapi import Depends
from redis.asyncio import Redis

from core.config import settings
from db.redis.factory import get_redis
from services.producer.message_builder import MessageBuilder


class BetRedisProducer:

    def __init__(self, redis: Redis) -> None:
        self.redis = redis

    @backoff.on_exception(**settings.backoff_config.model_dump())
    async def bulk_update_bet_state(self, task_name: str, event_id: str, state: int):
        message = MessageBuilder(task_name).build(event_id, state)
        await self.redis.publish(settings.channel_name, message.model_dump_json())


@lru_cache
def get_bet_producer(redis=Depends(get_redis)):
    return BetRedisProducer(redis=redis)
