from redis.asyncio import Redis

redis = {}


async def get_redis() -> Redis:
    return redis["client"]
