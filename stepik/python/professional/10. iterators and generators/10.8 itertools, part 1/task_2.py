import operator

from itertools import accumulate


def factorials(n):
    if n < 1:
        return 1
    return accumulate(range(1, n + 1), operator.mul)


# alt
def factorials(n):
    yield from accumulate(range(1, n + 1), lambda x, y: x * y)


numbers = factorials(2)

print(next(numbers))
print(next(numbers))
