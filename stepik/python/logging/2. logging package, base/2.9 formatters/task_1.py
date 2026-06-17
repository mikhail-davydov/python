import logging
import sys

all_level_handler = logging.StreamHandler(stream=sys.stdout)

error_level_handler = logging.StreamHandler(stream=sys.stderr)
error_level_handler.setLevel(logging.ERROR)
error_fmt = '%(levelname)s - %(threadName)s - [%(module)s:%(funcName)s] - %(message)s'
error_level_handler.setFormatter(logging.Formatter(fmt=error_fmt))

handlers = [
    all_level_handler,
    error_level_handler
]

logging.basicConfig(
    level=logging.DEBUG,
    format='%(levelname)s - %(message)s',
    handlers=handlers
)
