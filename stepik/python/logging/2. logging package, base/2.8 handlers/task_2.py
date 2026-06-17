import logging

all_level_handler = logging.FileHandler(filename='trace.log', encoding='ascii', errors='replace')

errors_handler = logging.FileHandler(filename='errors.log', encoding='ascii', errors='replace', delay=True)
errors_handler.setLevel(logging.ERROR)

handlers = [
    all_level_handler,
    errors_handler
]

logging.basicConfig(
    handlers=handlers,
    format="%(levelname)s - %(message)s",
    level=logging.DEBUG
)

# alt

import logging

log_params = {"encoding": "ascii", "errors": "replace"}

all_logs_handler = logging.FileHandler(filename="trace.log", **log_params)

error_logs_handler = logging.FileHandler(filename="errors.log", delay=True, **log_params)
error_logs_handler.setLevel(logging.ERROR)

logging.basicConfig(level=logging.DEBUG,
                    handlers=[all_logs_handler, error_logs_handler],
                    format="%(levelname)s - %(message)s"
                    )
