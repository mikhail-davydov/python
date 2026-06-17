import logging
import sys


def filter_out_warn_err(record: logging.LogRecord) -> bool:
    return not logging.INFO < record.levelno < logging.CRITICAL


stdout_handler = logging.StreamHandler(stream=sys.stdout)
stdout_handler.addFilter(filter_out_warn_err)

stderr_handler = logging.StreamHandler(stream=sys.stderr)
stderr_handler.setLevel(logging.WARNING)
stderr_formatter = logging.Formatter("%(levelname)s - %(threadName)s - [%(module)s:%(funcName)s] - %(message)s")
stderr_handler.setFormatter(stderr_formatter)

logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)s - %(message)s",
    handlers=[stdout_handler, stderr_handler]
)
