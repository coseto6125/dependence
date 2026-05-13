"""Smoke test: pyyaml — load/dump with anchors and aliases."""
import yaml

def test_pyyaml_anchor_alias_roundtrip():
    doc = """
app:
  name: enoract
  features:
    - search
    - retrieval
  config:
    max_retries: &max_retries 3
    timeout: *max_retries
"""
    data = yaml.safe_load(doc)
    assert data["app"]["config"]["timeout"] == 3
    output = yaml.safe_dump(data)
    reloaded = yaml.safe_load(output)
    assert reloaded["app"]["name"] == "enoract"