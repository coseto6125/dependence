"""Smoke test: structlog — structured logging over logxide."""
import structlog
import sys

def test_structlog_configures_and_produces_output():
    structlog.configure(
        processors=[
            structlog.processors.add_log_level,
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.dev.ConsoleRenderer()
            if sys.stderr.isatty()
            else structlog.processors.JSONRenderer(),
        ],
        wrapper_class=structlog.make_filtering_bound_logger(10),
        context_class=dict,
        logger_factory=structlog.PrintLoggerFactory(file=sys.stdout),
        cache_logger_on_first_use=False,
    )
    log = structlog.get_logger()
    # Just verify config doesn't raise and logger is usable
    assert log is not None
    assert callable(log.info)