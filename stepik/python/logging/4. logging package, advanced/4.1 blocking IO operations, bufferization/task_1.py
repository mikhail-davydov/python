import logging
import typing


class BufferingFileHandler(logging.FileHandler):
    def __init__(self, filename, mode='a', encoding=None, delay=False,
                 errors=None, capacity=1, flush_level=logging.ERROR,
                 ):
        self.capacity = capacity
        self._count_emit_records = 0
        self.flush_level = flush_level
        super().__init__(filename, mode, encoding, delay, errors)

    @typing.override
    def emit(self, record):
        if self.stream is None:
            if self.mode != 'w' or not self._closed:
                self.stream = self._open()
        if self.stream:
            self._emit(record)

    def _emit(self, record):
        self._count_emit_records += 1
        try:
            msg = self.format(record)
            stream = self.stream
            stream.write(msg + self.terminator)
            if self.should_flush(record):
                self.flush()
                self._count_emit_records = 0
        except RecursionError:
            raise
        except Exception:
            self.handleError(record)

    def should_flush(self, record):
        return (record.levelno >= self.flush_level or
                self._count_emit_records >= self.capacity)


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = BufferingFileHandler(filename='trace.log', encoding='utf-8', delay=True,
                               capacity=10, flush_level=logging.WARNING,
                               )
file_formatter = logging.Formatter(fmt='%(asctime)s [%(levelname)-8s] - %(message)s',
                                   datefmt='%Y-%m-%d %H:%M:%S',
                                   )
handler.setFormatter(file_formatter)
logger.addHandler(handler)
