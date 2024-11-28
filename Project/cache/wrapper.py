from functools import wraps

from flask import current_app

from cache.redis_cache import RedisCache

def fetch_from_cache(cache_name: str):
    cache_conn = RedisCache(current_app.config['redis'])
    def decorator(f):

        @wraps(f)
        def wrapper(*args, **kwargs):
            cache_conn.reconnect_if_need()
            cached_value = cache_conn.read(cache_name)
            if cached_value:
                return cached_value
            response = f(*args, **kwargs)
            cache_conn.set(cache_name,response)
            return response
        return wrapper
    return decorator