from itertools import islice


def take(iterable, n):
    return islice(iterable, n)


iterator = iter('beegeek')

print(*take(iterator, 1))