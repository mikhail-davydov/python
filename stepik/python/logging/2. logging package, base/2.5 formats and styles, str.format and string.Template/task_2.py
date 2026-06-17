import logging

import anyio
import loguru
import pytest
import sys

logging.basicConfig(
    stream=sys.stdout,
    level=logging.INFO,
    format='%(asctime)s - %(message)s: %(relativeCreated)d'
)

logging.info('done')

# alt

logging.basicConfig(level=logging.DEBUG,
                    stream=sys.stdout,
                    format="+$relativeCreated ms. $message", style="$"
                    )

logging.debug("прошло времени с начала выполнения программы")
