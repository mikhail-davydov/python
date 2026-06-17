from collections import defaultdict

import logging
import sys

logging.basicConfig(
    level=logging.DEBUG,
    stream=sys.stdout,
    format="%(levelname)8s: %(message)s"
)


class LogLevelStats(logging.Filter):
    def __init__(self):
        super().__init__()
        self.level_counter = defaultdict(int)

    def filter(self, record: logging.LogRecord) -> bool:
        self.level_counter[record.levelname] += 1
        return True


logger = logging.getLogger()
log_level_counter = LogLevelStats()
logger.addFilter(log_level_counter)

logging.debug("1")
logging.debug("2")
logging.warning("3")
logging.debug("4")
logging.info("5")
logging.info("6")
logging.info("7")
logging.warning("8")
logging.error("9")
logging.debug("10")

print('\nСтатистика с процентами:')
all_logs_count = sum(log_level_counter.level_counter.values())
for level, num in sorted(log_level_counter.level_counter.items()):
    print(f'{2 * ' '}{level}: {num} ({num / all_logs_count:.0%})')
