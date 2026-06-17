import logging
import sys

logging.basicConfig(
    level=logging.INFO,
    stream=sys.stdout,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def validate_config(config: dict) -> bool:
    try:
        if 'api_key' not in config:
            logging.warning("Отсутствует обязательный параметр: api_key", stack_info=True)
            return False
        if not config['api_key']:
            logging.warning("API ключ не может быть пустым", stack_info=True)
            return False
        return True

    except Exception:
        logging.error("Ошибка валидации конфигурации", exc_info=True, stack_info=True)
        return False


