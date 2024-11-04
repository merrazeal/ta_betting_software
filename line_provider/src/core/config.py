import os
from functools import lru_cache
from typing import Callable, Tuple

import aiohttp
import backoff
from pydantic_settings import BaseSettings
from redis.exceptions import ConnectionError as RedisConnectionError


class RedisPubsubConfig(BaseSettings):
    host: str = os.getenv("REDIS_PUBSUB_HOST")
    port: str = os.getenv("REDIS_PUBSUB_PORT")
    db: int = os.getenv("REDIS_PUBSUB_DB")


class BackoffConfig(BaseSettings):
    wait_gen: Callable = backoff.expo
    exception: Tuple = (aiohttp.ClientError, RedisConnectionError)
    max_tries: int = 3


class Settings(BaseSettings):
    project_name: str = os.getenv("PROJECT_NAME")
    redis_pubsub_config: RedisPubsubConfig = RedisPubsubConfig()
    channel_name: str = "bet_maker"
    elastic_url: str = os.getenv("ELASTIC_URL")
    event_index: str = "event"
    update_bets_state_task_name: str = "update_bets_state"
    backoff_config: BackoffConfig = BackoffConfig()


@lru_cache()
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
