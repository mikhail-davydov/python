def my_awesome_gen():
    total_sum = 0
    while True:
        value = yield total_sum  # всегда возвращаем накопленную сумму
        if isinstance(value, int):
            total_sum += value
        elif isinstance(value, float):
            total_sum *= value
        else:
            return "Ошибка: введите число типа int или float"


g = my_awesome_gen()

print(g.send(None))  # Выводит 0
print(g.send(10))  # Выводит 10
print(g.send(11))  # Выводит 21
print(g.send(0.5))  # Выводит 10.5
print(g.send(100))  # Выводит 110.5
print(g.send("ok"))  # Возбуждается ошибка StopIteration: Ошибка: введите число типа int или float

# alt

from typing import Generator, TypeAlias

T: TypeAlias = int | float


def my_awesome_gen() -> Generator[T, T, str]:
    value: T = 0
    while True:
        send_value = yield value
        match send_value:
            case int() as send_value:
                value += send_value
            case float() as send_value:
                value *= send_value
            case _:
                return 'Ошибка: введите число типа int или float'
