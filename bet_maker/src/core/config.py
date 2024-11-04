import os
from functools import lru_cache

from pydantic_settings import BaseSettings


class PostgresConfig(BaseSettings):
    username: str = os.getenv("POSTGRES_USER")
    password: str = os.getenv("POSTGRES_PASSWORD")
    host: str = os.getenv("POSTGRES_HOST")
    port: str = os.getenv("POSTGRES_PORT")
    database_name: str = os.getenv("POSTGRES_DB")


class RedisPubsubConfig(BaseSettings):
    host: str = os.getenv("REDIS_PUBSUB_HOST")
    port: str = os.getenv("REDIS_PUBSUB_PORT")
    db: int = os.getenv("REDIS_PUBSUB_DB")


class APILineProviderConfig(BaseSettings):
    list_event_url: str = os.getenv("LIST_EVENT_URL")
    detail_event_url: str = os.getenv("DETAIL_EVENT_URL")


class Settings(BaseSettings):
    postgres_config: PostgresConfig = PostgresConfig()
    redis_pubsub_config: RedisPubsubConfig = RedisPubsubConfig()
    project_name: str = os.getenv("PROJECT_NAME")
    message_poll_interval: int = 5
    message_execute_interval: int = 30
    channel_name: str = "bet_maker"
    api_line_provider_config: APILineProviderConfig = APILineProviderConfig()


@lru_cache()
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
