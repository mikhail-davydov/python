import datetime

import logging
from logging.handlers import TimedRotatingFileHandler


def get_logger() -> logging.Logger:
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.ERROR)
    logger.propagate = False

    handler = TimedRotatingFileHandler(
        filename='error.log',
        encoding='u8',
        when='w0',
        atTime=datetime.time(3, 30),
        backupCount=2
    )
    formatter = logging.Formatter(
        fmt='%(asctime)-30s [%(name)s %(levelname)8s] - %(message)s',
        datefmt='%y.%m.%d(%A)_%H:%M:%S'
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger
