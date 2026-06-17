import json
import logging

records: list[logging.LogRecord] = []

with open("records.jsonl", "w", encoding="utf-8") as file:
    for record in records:
        log_entry = {"levelname": record.levelname,
                     "name": record.name,
                     "taskName": record.taskName,
                     "message": record.getMessage()}
        json_string = json.dumps(log_entry, ensure_ascii=False)
        file.write(json_string + "\n")
