import logging

warn_counter = 0


def warning_counter(record: logging.LogRecord) -> bool:
    global warn_counter
    if record.levelno >= 30:
        warn_counter += 1
    return True


# logging.basicConfig(filename="trace.log",
#                     level=logging.DEBUG,
#                     encoding="utf-8",
#                     format="%(levelname)-8s - %(message)s")

logger_formatter = logging.Formatter(fmt='%(levelname)-8s - %(message)s')
logger_handler = logging.FileHandler(filename='trace.log', encoding='u8')
logger_handler.setFormatter(logger_formatter)

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.addFilter(warning_counter)
logger.addHandler(logger_handler)
