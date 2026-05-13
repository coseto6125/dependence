"""Smoke test: python-dotenv — load variables from .env file."""
import os
from pathlib import Path
from dotenv import load_dotenv

def test_dotenv_loads_env_file(tmp_path):
    env_file = tmp_path / ".env"
    env_file.write_text("SMOKE_VAR=hello_world\nSMOKE_FLAG=true\n")
    load_dotenv(env_file)
    assert os.getenv("SMOKE_VAR") == "hello_world"
    assert os.getenv("SMOKE_FLAG") == "true"