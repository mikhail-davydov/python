import json
import logging
import typing


class JSONFormatter(logging.Formatter):
    def __init__(self, keys_fmt=None):
        self.keys_fmt = keys_fmt

    @typing.override
    def format(self, record):
        dict_record = self._get_dict_record(record)
        s = json.dumps(dict_record, ensure_ascii=False, default=str)
        return s

    def _get_dict_record(self, record):
        dict_record = {}
        base_keys_fmt = {
            "created": "created",
            "levelname": "levelname",
            "name": "name",
            "message": "message",
        }
        keys_fmt = self.keys_fmt or base_keys_fmt
        record.message = record.getMessage()
        for k, v in keys_fmt.items():
            dict_record[k] = getattr(record, v)
        if record.exc_info:
            if not record.exc_text:
                record.exc_text = self.formatException(record.exc_info)
        if record.exc_text:
            dict_record["exc_text"] = record.exc_text
        if record.stack_info:
            dict_record["stack_info"] = self.formatStack(record.stack_info)
        return dict_record


file_handler = logging.FileHandler("logs.jsonl", encoding="utf-8")
json_formatter = JSONFormatter({"lvl": "levelname", "msg": "message"})
file_handler.setFormatter(json_formatter)
root = logging.getLogger()
root.setLevel(logging.INFO)
root.addHandler(file_handler)
