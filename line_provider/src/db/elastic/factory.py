from elasticsearch import AsyncElasticsearch

elastic = {}


async def get_elastic() -> AsyncElasticsearch:
    return elastic["client"]
