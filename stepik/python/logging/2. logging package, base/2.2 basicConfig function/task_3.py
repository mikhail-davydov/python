import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename='trace.log',
    encoding='u8',
    format=logging.BASIC_FORMAT,
)


def task(a: int, b: int) -> int:
    try:
        logging.debug(f'В функцию переданы аргументы: {a=}, {b=}')
        result = a + b
        logging.info(f'Функция вернула результат: {result=}')
        return result
    except TypeError as e:
        logging.error(f'Функция завершилась с исключением: {e!r}')
