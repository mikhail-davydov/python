import logging
import sys

stream_handler = logging.StreamHandler(stream=sys.stdout)
file_handler = logging.FileHandler(filename='app.log', encoding='ascii', errors='replace')

_handlers = [
    stream_handler,
    file_handler,
]

logging.basicConfig(
    format="%(levelname)s - %(message)s",
    handlers=_handlers,
    level=logging.INFO,
)
