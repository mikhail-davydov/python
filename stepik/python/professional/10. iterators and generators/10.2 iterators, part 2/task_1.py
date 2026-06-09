from typing import Callable, Union


def filterfalse(predicate: (Callable | None), iterable: Union[list, tuple, iter]) -> iter:
    return filter(lambda x: not bool(x) if predicate is None else not predicate(x), iterable)


numbers = (1, 2, 3, 4, 5)

print(*filterfalse(lambda x: x % 2 == 0, numbers))


# alt
def filterfalse(func, iterable):
    if func is None:
        func = bool
    return filter(lambda elem: not func(elem), iterable)
