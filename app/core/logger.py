import sys
from loguru import logger
import json

def serialize(record):
    subset = {
        "timestamp": record["time"].isoformat(),
        "level": record["level"].name,
        "message": record["message"],
        "extra": record["extra"]
    }
    return json.dumps(subset)

def patching(record):
    record["extra"]["serialized"] = serialize(record)

# Configuring logger
logger.remove()
# Add stdout handler with generic format or JSON
logger.add(sys.stderr, format="{time} | {level} | {message} | {extra}", level="INFO")
# Also log to file in JSON lines
logger.add("app.log", rotation="500 MB", serialize=True)

log = logger
