import json
import logging

# record = logging.LogRecord()

record_dict = {
    'created': record.created,
    'levelname': record.levelname,
    'name': record.name,
    'lineno': record.lineno,
    'funcName': record.funcName,
    'message': record.getMessage()
}

print(json.dumps(record_dict, ensure_ascii=False))
