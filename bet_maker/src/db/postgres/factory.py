from asyncpg import Pool

postgres = {}


async def get_pool() -> Pool:
    return postgres["pool"]
