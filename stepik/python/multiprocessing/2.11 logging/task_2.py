import logging
import sys

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

runtime_file_handler = logging.FileHandler(filename='runtime.log', encoding='u8')
runtime_file_handler.setLevel(logging.INFO)

runtime_formatter = logging.Formatter(fmt='%(asctime)s %(levelname)s %(message)s')
runtime_file_handler.setFormatter(runtime_formatter)
runtime_file_handler.addFilter(lambda record: record.levelno <= logging.WARNING)

errors_file_handler = logging.FileHandler(filename='errors.log', encoding='u8')
errors_file_handler.setLevel(logging.ERROR)

errors_formatter = logging.Formatter(fmt='%(asctime)s %(threadName)s %(message)s')
errors_file_handler.setFormatter(errors_formatter)

###
stream_handler = logging.StreamHandler(stream=sys.stdout)
stream_handler.setLevel(logging.INFO)
stream_handler.addFilter(lambda record: record.levelno <= logging.WARNING)
stream_handler.setFormatter(runtime_formatter)
###

logger.addHandler(runtime_file_handler)
logger.addHandler(errors_file_handler)
# logger.addHandler(stream_handler)

if __name__ == '__main__':
    logger.debug("Отладочное сообщение.")
    logger.info("Информационное сообщение.")
    logger.warning("Предупреждение!")
    logger.error("Внимание, ошибка!")
    logger.critical("Критическая ситуация!!!")


# alt

import logging


def set_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    file_info_handler = logging.FileHandler("runtime.log")
    file_err_handler = logging.FileHandler("errors.log")
    file_info_handler.setLevel(logging.INFO)
    file_err_handler.setLevel(logging.ERROR)

    file_info_handler.addFilter(lambda record: record.levelno <= logging.WARNING)
    formatter_info = logging.Formatter("$asctime $levelname $message", style="$")
    file_info_handler.setFormatter(formatter_info)
    formatter_err = logging.Formatter("$asctime $threadName $message", style="$")
    file_err_handler.setFormatter(formatter_err)

    logger.addHandler(file_info_handler)
    logger.addHandler(file_err_handler)

    return logger

logger = set_logger(__name__)

# alt

import logging

# дополните код
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

file_handler_runtime = logging.FileHandler("runtime.log", "w", encoding="utf-8")
formatter_runtime = logging.Formatter("$asctime $levelname $message", style="$")
file_handler_runtime.setFormatter(formatter_runtime)


file_handler_errors = logging.FileHandler("errors.log", "w", encoding="utf-8")
formatter_errors = logging.Formatter("$asctime $threadName $message", style="$")
file_handler_errors.setFormatter(formatter_errors)

class InfoAndWarningFilter(logging.Filter):
    def filter(self, record):
        return record.levelno in (logging.INFO, logging.WARNING)

class OtherFilter(logging.Filter):
    def filter(self, record):
        return record.levelno in (logging.DEBUG, logging.ERROR, logging.CRITICAL)

file_handler_runtime.addFilter(InfoAndWarningFilter())
file_handler_errors.addFilter(OtherFilter())


logger.addHandler(file_handler_runtime)
logger.addHandler(file_handler_errors)