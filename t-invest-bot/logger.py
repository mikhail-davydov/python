import logging


def get(name: str):
    logger = logging.getLogger(name)
    logging.basicConfig(
        format='%(asctime)s [%(levelname)s]::%(module)s:: %(message)s',
        level=logging.DEBUG
    )
    return logger
