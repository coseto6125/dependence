"""Smoke test: sanic — async HTTP app framework."""
from sanic import Sanic, text

app = Sanic("smoke-test")

@app.get("/ping")
async def ping(request):
    return text("pong")

def test_sanic_app_responds_pong():
    _, response = app.test_client.get("/ping")
    assert response.status == 200
    assert response.text == "pong"