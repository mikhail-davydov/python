import logging
import multiprocessing
from collections.abc import Callable


def set_logger(name: str, func_name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    if logger.handlers:
        return logger
    logger.setLevel(logging.DEBUG)
    file_handler = logging.FileHandler(filename='log.txt', encoding='u8')
    file_formatter = logging.Formatter(fmt=f'%(processName)s, %(threadName)s, {func_name}, %(asctime)s')
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)
    return logger


def logged(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        queue = kwargs.pop('log_queue', None)  # <-!
        logger = set_logger(multiprocessing.current_process().name, func.__name__)  # <-!
        logger.debug('')
        try:
            result = func(*args, **kwargs)
            return result
        except BaseException as exc:
            raise

    return wrapper


# alt

import logging
from functools import wraps


def set_logger() -> logging.Logger:
    logger = logging.getLogger('__name__')
    if logger.handlers:
        return logger
    logger.setLevel(logging.INFO)

    file_handler = logging.FileHandler('log.txt', 'a', encoding='utf-8')
    file_handler.setLevel(logging.INFO)
    formatter = logging.Formatter('$processName, $threadName, $message, $asctime', style='$')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger


def logged(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger = set_logger()
        logger.info(func.__name__)
        return func(*args, **kwargs)

    return wrapper
