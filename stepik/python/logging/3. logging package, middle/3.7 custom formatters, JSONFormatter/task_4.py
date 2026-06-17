import json
import logging
import typing

LOG_RECORD_BUILTIN_ATTRS = {"args", "asctime", "created", "exc_info", "exc_text",
                            "filename", "funcName", "levelname", "levelno", "lineno",
                            "module", "msecs", "message", "msg", "name",
                            "pathname", "process", "processName", "relativeCreated", "stack_info",
                            "thread", "threadName", "taskName"}


class JSONFormatter(logging.Formatter):
    def __init__(self, keys_fmt=None, **kwargs):
        super().__init__(**kwargs)
        self.keys_fmt = keys_fmt

    @typing.override
    def format(self, record):
        dict_record = self._get_dict_record(record)
        s = json.dumps(dict_record, ensure_ascii=False, default=str)
        return s

    def _get_dict_record(self, record):
        dict_record = {}
        base_keys_fmt = {"created": "created",
                         "levelname": "levelname",
                         "name": "name",
                         "message": "message"}
        keys_fmt = self.keys_fmt or base_keys_fmt
        record.message = record.getMessage()
        record.asctime = self.formatTime(record, self.datefmt)
        for k, v in keys_fmt.items():
            dict_record[k] = getattr(record, v)
        if record.exc_info:
            if not record.exc_text:
                record.exc_text = self.formatException(record.exc_info)
        if record.exc_text:
            dict_record["exc_text"] = record.exc_text
        if record.stack_info:
            dict_record["stack_info"] = self.formatStack(record.stack_info)
        for k, v in record.__dict__.items():
            if k not in LOG_RECORD_BUILTIN_ATTRS:
                dict_record[k] = v
        return dict_record


handler = logging.FileHandler("logs.jsonl", encoding="utf-8")
json_formatter = JSONFormatter({"time": "asctime", "lvl": "levelname", "msg": "message"}, datefmt="%FT%X%z")
handler.setFormatter(json_formatter)

logger = logging.getLogger(__name__)
logger.addHandler(handler)

logger.info("Информационное сообщение")
logger.warning("Предупреждение. Пользователь %s трижды ввел неверный пароль", "user_123")


def foo():
    try:
        1 / 0
    except Exception as exc:
        logger.exception("Ошибка: %s", repr(exc))


logger.critical("Потеря соединения с основным кластером БД! Сервисы недоступны!",
                extra={'service': 'postgresql-cluster', 'downtime_seconds': 45}
                )
