from itertools import chain, tee


def ncycles(iterable, times):
    return chain.from_iterable(tee(iterable, times))


# alt
def ncycles(iterable, times: int):
    iterable = tuple(iterable)
    for _ in range(times):
        yield from iterable


print(*ncycles([1, 2, 3, 4], 3))

iterator = iter('bee')
print(*ncycles(iterator, 4))

iterator = iter([1])
print(*ncycles(iterator, 10))
