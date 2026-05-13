"""Smoke test: psqlpy — async PostgreSQL driver (import + pool interface check)."""
import psqlpy
import inspect

def test_psqlpy_connect_pool_has_expected_params():
    sig = inspect.signature(psqlpy.connect_pool)
    params = list(sig.parameters.keys())
    assert "host" in params
    assert "password" in params
    assert "db_name" in params
    assert callable(psqlpy.connect_pool)

def test_psqlpy_connection_class_accessible():
    assert hasattr(psqlpy, "Connection")
    assert hasattr(psqlpy, "ConnectionPool")