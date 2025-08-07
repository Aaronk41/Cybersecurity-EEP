import json
import base64


MSG_TYPE_CHAT = "chat"
MSG_TYPE_COMMAND = "command"
MSG_TYPE_ENCRYPTED = "encrypted"

def wrap_message(msg_type, sender, content):
    """Encodes a message in a structured JSON format."""
    return json.dumps({
        "type": msg_type,
        "sender": sender,
        "content": base64.b64encode(content).decode() 
    }).encode()

def unwrap_message(raw_data):
    """Decodes a structured message back into components."""
    try:
        msg = json.loads(raw_data.decode())
        return msg["type"], msg["sender"], base64.b64decode(msg["content"])
    except Exception as e:
        print(f"[ERROR] Failed to unwrap message: {e}")
        return None, None, None
