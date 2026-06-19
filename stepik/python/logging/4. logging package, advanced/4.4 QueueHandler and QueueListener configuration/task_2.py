import atexit
import logging.config
import yaml
from logging.handlers import QueueListener


def auto_queue_listener(queue, *handlers, respect_handler_level=False):
    queue_listener = QueueListener(queue, *handlers, respect_handler_level=respect_handler_level)
    queue_listener.start()
    atexit.register(queue_listener.stop)
    return queue_listener


with open("config.yaml", 'r', encoding='utf-8') as f:
    dict_config = yaml.safe_load(f)

logging.config.dictConfig(dict_config)
