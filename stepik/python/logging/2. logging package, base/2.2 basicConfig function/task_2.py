import sys

import logging

logging.basicConfig(
    level=logging.DEBUG,
    stream=sys.stdout,
    format=logging.BASIC_FORMAT.replace(':', ' | ')
)

logging.debug('debug')
logging.info('info')