# Модуль main.py

import logging
import requests
import sys

logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
logger = logging.getLogger(__name__)


def fetch_url(url: str) -> requests.Response | None:
    """Выполняет GET-запрос по указанному URL с логированием."""
    logger.debug("Запрос по адресу %s", url)
    try:
        response = requests.get(url, timeout=5)
        logger.info("Получен ответ. Код: %d, URL: %s", response.status_code, url)
        return response
    except requests.exceptions.RequestException as exc:
        logger.error("Ошибка запроса: %s", exc)


def print_loggers_recursive(logger, depth=0):
    """Рекурсивно обходит всех детей логгера"""
    indent = "\t" * depth  # смещение для наглядности

    # Выводим текущий логгер
    print(f"{indent}{logger}")

    # Рекурсивно обходим потомков
    for child in logger.getChildren():
        print_loggers_recursive(child, depth + 1)


if __name__ == '__main__':
    fetch_url("http://www.google.com")
    print("Полная иерархия логгеров:")
    root_logger = logging.getLogger()
    print_loggers_recursive(root_logger)
