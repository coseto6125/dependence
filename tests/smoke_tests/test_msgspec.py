"""Smoke test: msgspec — struct validation + json encode/decode."""
import msgspec

class ChatMessage(msgspec.Struct):
    role: str
    content: str

def test_msgspec_struct_encode_decode():
    msg = ChatMessage(role="user", content="hello")
    encoded = msgspec.json.encode(msg)
    decoded = msgspec.json.decode(encoded, type=ChatMessage)
    assert decoded.role == "user"
    assert decoded.content == "hello"