import copy
import logging
import sys


def mask_card_number(record: logging.LogRecord):
    stdout_record = copy.copy(record)
    if hasattr(stdout_record, 'card_number'):
        stdout_record.card_number = stdout_record.card_number[:-4] + 4 * '*'
    return stdout_record


log_format = "%(levelname)s - %(message)s - [%(card_number)s;%(amount)s;%(currency)s]"
log_formatter = logging.Formatter(
    fmt=log_format,
    defaults={"card_number": "NULL", "amount": "NULL", "currency": "NULL"}
)

stdout_handler = logging.StreamHandler(stream=sys.stdout)
stdout_handler.setFormatter(log_formatter)
stdout_handler.addFilter(mask_card_number)

file_handler = logging.FileHandler(filename='trace.log', encoding='u8')
file_handler.setFormatter(log_formatter)

logging.basicConfig(
    level=logging.DEBUG,
    handlers=[stdout_handler, file_handler]
)
