import calendar
import locale

locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')


def get_weekday(number: int) -> str:
    if not isinstance(number, int):
        raise TypeError('Аргумент не является целым числом')
    if number not in range(1, 8):
        raise ValueError('Аргумент не принадлежит требуемому диапазону')
    return calendar.day_name[number - 1].title()


try:
    print(get_weekday(8))
except ValueError as err:
    print(err)
    print(type(err))
