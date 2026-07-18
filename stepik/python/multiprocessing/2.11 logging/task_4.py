import concurrent.futures
import logging


def set_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.ERROR)
    file_handler = logging.FileHandler(filename='log_errors.txt', encoding='u8')
    file_formatter = logging.Formatter(fmt='%(processName)s, %(asctime)s, %(message)s')
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)
    return logger


def handler(url: str) -> str:
    logger = set_logger(__name__)
    func_name = __name__
    try:
        func_name = get_image.__name__
        file = get_image(url)
        func_name = image_processing.__name__
        return image_processing(file)
    except Exception as err:
        logger.error(f'{func_name}, {err!s}')


def callback_save(future: concurrent.futures.Future) -> None:
    logger = set_logger(__name__)
    func_name = __name__
    try:
        new_file = future.result()
        func_name = save_image.__name__
        save_image(new_file)
    except Exception as err:
        logger.error(f'{func_name}, {err!s}')


def group_image_processing(file_source: str) -> None:
    with open(file_source) as file:
        urls = file.read().split()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for url in urls:
            future = executor.submit(handler, url)
            future.add_done_callback(callback_save)


# alt

import concurrent.futures
import multiprocessing
import logging

from functools import wraps
from typing import Callable

logger = multiprocessing.get_logger()
logger.setLevel(logging.ERROR)

file_handler = logging.FileHandler('log_errors.txt')
file_handler.setFormatter(logging.Formatter(fmt='{processName}, {asctime}, {message}', style='{'))

logger.addHandler(file_handler)


def error_loger(func: Callable, logger=logger):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as error:
            logger.error(f'{func.__name__}, {error}')

    return wrapper


def handler(url: str) -> str:
    file = get_image(url)
    return image_processing(file)


def callback_save(future: concurrent.futures.Future) -> None:
    new_file = future.result()
    save_image(new_file)


def group_image_processing(file_source: str) -> None:
    with open(file_source) as file:
        urls = file.read().split()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for url in urls:
            future = executor.submit(handler, url)
            future.add_done_callback(callback_save)


if __name__ == '__main__':
    get_image = error_loger(get_image)
    image_processing = error_loger(image_processing)
    save_image = error_loger(save_image)
