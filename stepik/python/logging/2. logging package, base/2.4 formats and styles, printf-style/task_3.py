import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename='app.log',
    encoding='u8',
    format='[%(levelname)-8s] %(relativeCreated)+010d %(processName)16s.%(funcName)-14s line:%(lineno) 04d - %(message)s'
)

logging.debug('debug')
logging.info('info')
logging.error('error')
logging.critical('critical')


def calc_sum(*args):
    logging.debug('внутри функции')
    return sum(args)


print(calc_sum(1, 2, 3))
