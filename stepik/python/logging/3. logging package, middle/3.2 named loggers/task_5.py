import logging
import requests
import sys

logging.basicConfig(level=logging.DEBUG,
                    stream=sys.stdout,
                    format="[%(levelname)-8s] - %(name)s - [url: %(url)s - %(message)s]"
                    )

logger = logging.getLogger("my_app")


def fetch_url(url: str) -> requests.Response | None:
    """Выполняет GET-запрос по указанному URL с логированием."""
    ctx = {"url": url}
    logger.debug("Инициализация запроса", extra=ctx)
    try:
        response = requests.get(url, timeout=1)
        logger.info("Получен ответ. Код: %d", response.status_code, extra=ctx)
        return response
    except requests.exceptions.RequestException as exc:
        error_type = exc.__class__.__name__
        logger.error("%s при запросе", error_type, extra=ctx)


if __name__ == '__main__':
    root = logging.getLogger()
    for child in root.getChildren():
        if child is not logger:
            child.setLevel(logging.CRITICAL)
    # function call
    print(fetch_url('https://google.com').status_code)
