import json
import logging
import typing


class JSONFormatter(logging.Formatter):

    @typing.override
    def format(self, record):
        dict_record = self._get_dict_record(record)
        s = json.dumps(dict_record, ensure_ascii=False)
        return s

    def _get_dict_record(self, record):
        dict_record = {"levelname": record.levelname,
                       "name": record.name,
                       "funcName": record.funcName,
                       "message": record.getMessage()}
        if record.exc_info:
            if not record.exc_text:
                record.exc_text = self.formatException(record.exc_info)
        if record.exc_text:
            dict_record["exc_text"] = record.exc_text
        if record.stack_info:
            dict_record["stack_info"] = self.formatStack(record.stack_info)
        return dict_record


handler = logging.FileHandler("app.log.jsonl", encoding="utf-8")
json_formatter = JSONFormatter()
handler.setFormatter(json_formatter)

logger = logging.getLogger(__name__)
logger.addHandler(handler)

logger.warning("Предупреждение %s", "!!")
try:
    1 / 0
except Exception as exc:
    logger.exception("Ошибка: %s", repr(exc), stack_info=True)
