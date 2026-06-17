import logging
import sys

logging.basicConfig(
    level=logging.INFO,
    stream=sys.stdout,
    format="{asctime}{levelname:^12}{funcName:.<10.10}{lineno:.>6} -> {message}",
    style="{"
)

logging.warning("123456")
logging.error("123456")
logging.info("123456")
