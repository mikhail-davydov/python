import time


def calculate_it(func, *args):
    start = time.perf_counter()
    result = func(*args) if args else func()
    end = time.perf_counter()
    return result, end - start


def get_the_fastest_func(funcs, arg):
    return min(funcs, key=lambda func: calculate_it(func, arg)[1] if arg else calculate_it(func)[1])


#


def for_and_append(iterable):  # с использованием цикла for и метода append()
    result = []
    for elem in iterable:
        result.append(elem)
    return result


def list_comprehension(iterable):  # с использованием списочного выражения
    return [elem for elem in iterable]


def list_function(iterable):  # с использованием встроенной функции list()
    return list(iterable)


print(get_the_fastest_func([for_and_append, list_comprehension, list_function], range(100_000)))
