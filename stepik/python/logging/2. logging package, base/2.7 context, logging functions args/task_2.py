import logging
import sys
from functools import wraps

FORMAT = "%(asctime)s - %(levelname)-8s - %(function)-10.10s - args: %(a)s - kwargs: %(kw)s - %(message)s"
logging.basicConfig(
    stream=sys.stdout,
    # filename="trace.log",
    # encoding="utf-8",
    level=logging.DEBUG,
    format=FORMAT
)


def trace(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        _extra = {
            'function': func.__name__,
            'a': args,
            'kw': kwargs
        }
        logging.debug("Вызов функции", extra=_extra)
        try:
            result = func(*args, **kwargs)
            logging.info("Функция завершилась успешно с результатом %s", result, extra=_extra)
            return result
        except Exception as exc:
            logging.error("Функция завершилась исключением %s", repr(exc), exc_info=True, extra=_extra)

    return wrapper


@trace
def sum_args(*args):
    return sum(args)


@trace
def raise_error():
    raise TypeError


sum_args(1, 2, 3)
raise_error()
