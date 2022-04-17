import pytest

from app.core.core import get_async_redis_connection


@pytest.fixture
async def redis_client():
    client = await get_async_redis_connection()
    yield client


@pytest.mark.asyncio
async def test_main(redis_client):
    client = await redis_client
    await client.set(name='test', value='test_value')
    res = await client.get('test')
    assert res == 'test_value'
