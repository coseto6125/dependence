"""Smoke test: logxide — Rust-backed stdlib logging drop-in."""
import logxide

def test_logxide_getlogger_returns_rust_backed_logger():
    logger = logxide.getLogger("smoke")
    assert hasattr(logxide, "_logxide_ext")  # Rust extension loaded
    assert hasattr(logger, "info")

def test_logxide_handlers_available():
    assert hasattr(logxide, "StreamHandler")
    assert hasattr(logxide, "FileHandler")
    assert hasattr(logxide, "RustFormatter")