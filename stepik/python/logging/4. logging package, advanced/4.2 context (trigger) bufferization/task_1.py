from collections import deque

import logging.handlers
import typing


class ContextMemoryHandler(logging.handlers.MemoryHandler):
    def __init__(self, capacity=0, flushLevel=logging.ERROR, target=None, flushOnClose=True):
        super().__init__(capacity=capacity, flushLevel=flushLevel, target=target, flushOnClose=flushOnClose)
        self.buffer: deque = deque(maxlen=self.capacity + 1)

    @typing.override
    def shouldFlush(self, record):
        return record.levelno >= self.flushLevel


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(filename='trace.log', encoding='utf-8', delay=True)
file_formatter = logging.Formatter(fmt='[%(levelname)-8s] - %(message)s')
file_handler.setFormatter(file_formatter)

context_handler = ContextMemoryHandler(
    capacity=5,
    target=file_handler, flushLevel=logging.WARNING,
    flushOnClose=False,  # не сбрасываем буфер при завершении
)
logger.addHandler(context_handler)
