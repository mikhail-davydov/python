import logging
import queue
import sys
from logging.handlers import QueueHandler, QueueListener

log_queue = queue.Queue()

deb_format = logging.Formatter("%(levelname)s - %(message)s")
err_format = logging.Formatter("%(levelname)s - %(threadName)s - [%(module)s:%(funcName)s] - %(message)s")

stdout_handler = logging.StreamHandler(stream=sys.stdout)
stdout_handler.setFormatter(deb_format)

stderr_handler = logging.StreamHandler(stream=sys.stderr)
stderr_handler.setFormatter(err_format)
stderr_handler.setLevel(logging.ERROR)

q_handler = QueueHandler(log_queue)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(q_handler)

listener = QueueListener(log_queue, stdout_handler, stderr_handler, respect_handler_level=True)
listener.start()

try:
    main()
finally:
    listener.stop()
