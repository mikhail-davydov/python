import logging
import sys

stdout_handler = logging.StreamHandler(stream=sys.stdout)
stdout_format = "%(levelname)s - %(message)s - [%(card_number)s;%(amount)s;%(currency)s]"
stdout_formatter = logging.Formatter(fmt=stdout_format,
                                     defaults={"card_number": "NULL", "amount": "NULL", "currency": "NULL"}
                                     )
stdout_handler.setFormatter(stdout_formatter)


def mask_card_number(record: logging.LogRecord) -> bool:
    if hasattr(record, 'card_number'):
        record.card_number = record.card_number[:-4] + 4 * '*'
    return True


logger = logging.getLogger()
logger.addFilter(mask_card_number)

logging.basicConfig(
    level=logging.DEBUG,
    handlers=[stdout_handler]
)

logging.warning(
    'Крупная транзакция требует проверки',
    extra={
        'card_number': '3782 822463 12345',
        'amount': 100000,
        'currency': 'RUB'
    }
)
logging.info('Платежный шлюз перезапущен')
logging.debug('Проверка доступности средств', extra={'card_number': '2222 3333 4444 5555'})

logging.error(
    'Ошибка при обработке платежа', extra={
        'card_number': '4111 1234 5678 9012',
        'amount': 5000,
        'currency': 'RUB'
    }
)


# alt

def card_filter(record: logging.LogRecord) -> bool:
    if hasattr(record, "card_number"):
        record.card_number = record.card_number[:-4] + "****"
    return True


stdout_handler = logging.StreamHandler(stream=sys.stdout)
stdout_format = "%(levelname)s - %(message)s - [%(card_number)s;%(amount)s;%(currency)s]"
stdout_formatter = logging.Formatter(fmt=stdout_format,
                                     defaults={"card_number": "NULL", "amount": "NULL", "currency": "NULL"}
                                     )
stdout_handler.setFormatter(stdout_formatter)
stdout_handler.addFilter(card_filter)

logging.basicConfig(level=logging.DEBUG,
                    handlers=[stdout_handler]
                    )
