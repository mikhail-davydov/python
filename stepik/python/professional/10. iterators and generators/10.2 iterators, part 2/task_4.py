from typing import Callable, Sequence, Collection


def starmap(func: Callable, iterable: Sequence[Collection]) -> iter:
    return map(func, *zip(*iterable))


points = [(1, 1, 1), (1, 1, 2), (2, 2, 3)]

print(*starmap(lambda x, y, z: x * y * z, points))


# alt
def starmap(func, iterable):
    return map(lambda args: func(*args), iterable)
