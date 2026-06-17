import logging
import sys

logging.basicConfig(
    level=logging.INFO,
    stream=sys.stderr,
    format='%(asctime)s | %(levelname)s | %(module)s | %(message)s'
)

logging.info('test')
