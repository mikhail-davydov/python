import logging

logging.basicConfig(
    format='Время: %(asctime)s.%(msecs)d %(message)s',
    datefmt='%p %I:%M:%S'
)

logging.warning("Сообщение!")
