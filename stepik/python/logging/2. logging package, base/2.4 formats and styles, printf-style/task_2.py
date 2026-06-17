import logging
import sys

logging.basicConfig(
    level=logging.INFO,
    stream=sys.stdout,
    format='%(asctime)s | %(levelname)-8s | %(module)s | %(lineno)04d | %(message)s'
)

logging.debug('debug')
logging.info('info')
logging.error('error')
logging.critical('critical')
