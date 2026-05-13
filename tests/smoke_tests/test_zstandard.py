"""Smoke test: zstandard — high-ratio compressor."""
import zstandard as zstd

def test_zstandard_compress_decompress_roundtrip():
    data = b"hello world " * 100
    ctx = zstd.ZstdCompressor(level=3)
    compressed = ctx.compress(data)
    decompressed = zstd.decompress(compressed)
    assert decompressed == data
    ratio = len(compressed) / len(data)
    assert ratio < 1.0