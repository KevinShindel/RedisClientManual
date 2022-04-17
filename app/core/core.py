from redis import Redis
from aioredis import Redis as AsyncRedis
from app.core.settings import (REDIS_PORT,
                               REDIS_HOST,
                               REDIS_PASSWORD,
                               REDIS_USERNAME,
                               REDIS_DB,
                               REDIS_CLOUD_HOST,
                               REDIS_CLOUD_PORT,
                               REDIS_CLOUD_PASS,
                               REDIS_CLOUD_USERNAME,
                               REDIS_CLOUD_DB)


def get_redis_connection(hostname=REDIS_HOST,
                         port=REDIS_PORT,
                         username=REDIS_USERNAME,
                         password=REDIS_PASSWORD,
                         db=REDIS_DB):
    """ Sync version of Redis client using redis-py library """
    client_kwargs = {
        "host": hostname,
        "port": port,
        "decode_responses": True,
        "db": db
    }
    if password:
        client_kwargs["password"] = password
    if username:
        client_kwargs["username"] = username

    return Redis(**client_kwargs)


async def get_async_redis_connection():
    """ ASYNC version Redis client using aioredis library"""
    client_redis = await AsyncRedis(host=REDIS_HOST,
                                    port=REDIS_PORT,
                                    db=REDIS_DB,
                                    password=REDIS_PASSWORD,
                                    username=REDIS_USERNAME,
                                    decode_responses=True)
    return client_redis


def get_cloud_redis_connection():
    """ cloud Redis client using redis client """
    client_redis = Redis(host=REDIS_CLOUD_HOST,
                         port=REDIS_CLOUD_PORT,
                         db=REDIS_CLOUD_DB,
                         password=REDIS_CLOUD_PASS,
                         username=REDIS_CLOUD_USERNAME,
                         decode_responses=True)
    return client_redis
