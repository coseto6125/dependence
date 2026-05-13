"""Smoke test: uvloop — fast asyncio event loop."""
import asyncio
import uvloop

def test_uvloop_installed_and_runs_task():
    uvloop.install()
    async def task():
        await asyncio.sleep(0)
        return 42
    result = asyncio.run(task())
    assert result == 42