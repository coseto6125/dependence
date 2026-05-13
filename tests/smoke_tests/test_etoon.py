"""Smoke test: etoon — TOON line encoding for structured logging."""
import etoon

def test_etoon_dumps_produces_toon_string():
    data = {"msg": "hello", "level": "info", "count": 42}
    encoded = etoon.dumps(data)
    assert isinstance(encoded, str)
    assert "hello" in encoded
    assert "info" in encoded
    assert "msg: hello" in encoded
    assert "count: 42" in encoded