from logging import handlers

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

log_hamdler = handlers.RotatingFileHandler(
    filename='app.log',
    encoding='u8',
    maxBytes=200,
    backupCount=2
)
log_formatter = logging.Formatter(
    fmt='[%(name)-5s] - [%(levelname)-8s] - %(message)s'
)
log_hamdler.setFormatter(log_formatter)
logger.addHandler(log_hamdler)
