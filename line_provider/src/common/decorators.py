# import functools
# import hashlib
# import logging
# from typing import Callable


# def cache_func_result(async_cache_adapter, ttl: int | None = None):
#     def decorator(func: Callable):
#         @functools.wraps(func)
#         async def wrapper(*args, **kwargs):
#             cache_key = f'{func.__name__}_{hashlib.sha256(str(args + tuple(kwargs.items())).encode()).hexdigest()}'
#             cached_result = await async_cache_adapter.get(cache_key)
#             if cached_result:
#                 logging.info(f'Retrieved cached result for function {func.__name__}.')
#                 return cached_result
#             result = await func(*args, **kwargs)
#             await async_cache_adapter.set(cache_key, result, ttl)
#             return result
#         return wrapper
#     return decorator

# TODO: AsyncCacheAdapter
