import logging
import sys

logging.basicConfig(
    stream=sys.stdout,
    level=logging.ERROR,
    encoding='u8',
    format='%(module)s -> %(processName)s -> %(threadName)s: %(message)s',
)


def main():
    logging.critical("Аварийное завершение работы!")


if __name__ == '__main__':
    main()

# alt

import logging
import sys

config_log = {
    "level": logging.ERROR,
    "stream": sys.stdout,
    "encoding": "utf-8",
    "format": "$module -> $processName -> $threadName: $message",
    "style": "$",
}

logging.basicConfig(**config_log)
