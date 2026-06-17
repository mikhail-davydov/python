import json
import logging
import sys

ALARM = 35
logging.addLevelName(ALARM, "ALARM")


def alarm(self, message, *args, **kwargs):
    if self.isEnabledFor(ALARM):
        self._log(ALARM, message, args, **kwargs)


logging.Logger.alarm = alarm

stdout_formatter = logging.Formatter(fmt='%(levelname)s - %(message)s')
stdout_handler = logging.StreamHandler(stream=sys.stdout)
stdout_handler.setFormatter(stdout_formatter)

root_logger = logging.getLogger()
root_logger.setLevel(logging.WARNING)
root_logger.addHandler(stdout_handler)

logging.basicConfig(
    level=logging.WARNING,
    format='%(levelname)s - %(message)s'
)

# alt

TRACE = 5
NOTICE = 25

logging.addLevelName(TRACE, "TRACE")
logging.addLevelName(NOTICE, "NOTICE")


def trace(self, message, *args, **kwargs):
    if self.isEnabledFor(TRACE):
        self._log(TRACE, message, args, **kwargs)


def notice(self, message, *args, **kwargs):
    if self.isEnabledFor(NOTICE):
        self._log(NOTICE, message, args, **kwargs)


logging.Logger.trace = trace
logging.Logger.notice = notice


# Упрощенная версия для примера
class JSONFormatter(logging.Formatter):
    @staticmethod
    def _get_dict_record(record):
        return {"level": record.levelname,
                "message": record.getMessage(),
                "name": record.name}

    def format(self, record):
        return json.dumps(self._get_dict_record(record), ensure_ascii=False)


handler = logging.StreamHandler(stream=sys.stdout)
handler.setFormatter(JSONFormatter())

logger = logging.getLogger()
logger.addHandler(handler)
logger.setLevel(TRACE)  # Включаем самый детальный уровень

# Проверяем
logger.trace("Вход в функцию foo()")  # Уровень 5
logger.debug("Отладочная информация")  # Уровень 10
logger.info("Запрос обработан")  # Уровень 20
logger.notice("Пользователь ввел неверный email")  # Уровень 25
logger.warning("Высокая нагрузка")  # Уровень 30
