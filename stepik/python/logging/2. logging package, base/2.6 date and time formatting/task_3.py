import logging

logging.basicConfig(
    format='%(asctime)s %(message)s',
    datefmt='%Y-%m-%dT%H:%M:%S%z'
)

logging.warning("Событие с часовым поясом")