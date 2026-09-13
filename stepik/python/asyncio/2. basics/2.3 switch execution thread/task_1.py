def task_1():
    for i in range(1, 5):
        yield i


def task_2():
    for s in "AB":
        yield s


g1 = task_1()
g2 = task_2()

from typing import Generator


def task_manager(gen_list: tuple[Generator, ...] | list[Generator]) -> None:
    gen_list = list(gen_list)
    while gen_list:
        task = gen_list.pop(0)
        try:
            print(next(task))
        except StopIteration:
            print(f'Задача {task.__name__} завершена!')
        else:
            gen_list.append(task)


if __name__ == '__main__':
    task_manager((g1, g2))
