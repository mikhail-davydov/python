import logging
import sys

stream_handler = logging.StreamHandler(stream=sys.stdout)
stream_format = '%(levelname)s - %(user_id)s - %(action)s - %(source)s - %(message)s'
stream_defaults = {
    'user_id': 'guest',
    'action': 'system',
    'source': 'internal'
}
stream_formatter = logging.Formatter(fmt=stream_format, defaults=stream_defaults)
stream_handler.setFormatter(stream_formatter)

logging.basicConfig(
    level=logging.DEBUG,
    handlers=[stream_handler]
)

logging.info("Роль не найдена", extra={'user_id': 12345})
logging.warning("Не удалось определить идентификатор пользователя в сессии")
