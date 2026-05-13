"""Smoke test: stamina — retry policy with exponential back-off."""
import asyncio
import stamina

attempt = 0

@stamina.retry(on=Exception, wait_max=0.05, wait_exp_base=2)
async def flaky():
    global attempt
    attempt += 1
    if attempt < 3:
        raise ValueError("not ready")
    return "done"

def test_stamina_retry_succeeds_on_third_attempt():
    global attempt
    attempt = 0
    result = asyncio.run(flaky())
    assert result == "done"
    assert attempt == 3