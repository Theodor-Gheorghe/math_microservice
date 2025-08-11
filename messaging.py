import json
from datetime import datetime

LOG_FILE = 'messages/messages.jsonl'

def persist_message(operation, input_data, result):
    """
    Simulates sending an event to a messaging system.
    Each request is saved as JSON in a .jsonl log file.
    """
    event = {
        'timestamp': datetime.now().isoformat(),
        'operation': operation,
        'input': input_data,
        'result': result
    }

    with open(LOG_FILE, 'a') as f:
        f.write(json.dumps(event) + '\n')