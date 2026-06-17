import logging
import sys


class RecordCounter:
    def __init__(self):
        self.counter = 0

    def filter(self, record) -> bool:
        self.counter += 1
        return True


logging.basicConfig(
    level=logging.INFO,
    stream=sys.stdout
)
logger = logging.getLogger()
record_counter = RecordCounter()
logger.addFilter(record_counter)

for i in range(1, 11):
    logging.info(i)

print(f"Всего залогировано событий: {record_counter.counter}")

# alt

import logging
import sys

record_count = 0


def record_counter(record: logging.LogRecord) -> bool:
    global record_count
    record_count += 1
    return True


logging.basicConfig(level=logging.INFO,
                    stream=sys.stdout
                    )
logger = logging.getLogger()
logger.addFilter(record_counter)

for i in range(1, 11):
    logging.info(i)

print(f"Всего залогировано событий: {record_count}")
