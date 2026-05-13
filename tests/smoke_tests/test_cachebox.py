"""Smoke test: cachebox — in-memory cache with TTL."""
import time
from cachebox import TTLCache

def test_cachebox_ttl_eviction():
    cache = TTLCache(maxsize=100, ttl=1.0)
    cache["key1"] = "value1"
    assert cache.get("key1") == "value1"
    time.sleep(1.1)
    assert cache.get("key1") is None  # expired

def test_cachebox_nested_value():
    cache = TTLCache(maxsize=100, ttl=10.0)
    cache["key2"] = {"nested": [1, 2, 3]}
    assert cache.get("key2") == {"nested": [1, 2, 3]}