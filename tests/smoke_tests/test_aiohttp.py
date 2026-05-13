"""Smoke test: aiohttp — async HTTP client (integration, requires network)."""
import pytest
import asyncio
import aiohttp

async def fetch_status():
    async with aiohttp.ClientSession() as session:
        async with session.get(
            "https://httpbin.org/get",
            timeout=aiohttp.ClientTimeout(total=5),
        ) as resp:
            return resp.status

@pytest.mark.integration
def test_aiohttp_get_returns_200():
    status = asyncio.run(fetch_status())
    assert status == 200