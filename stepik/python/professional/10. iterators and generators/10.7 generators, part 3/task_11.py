def pairwise(iterable):
    if not iterable:
        return
    it = iter(iterable)
    prev = next(it)

    for item in it:
        yield prev, item
        prev = item

    yield prev, None


# alt
def pairwise(iterable):
    it = iter(iterable)
    start = next(it, None)
    while not start is None:
        yield (start, start := next(it, None))


# alt
def pairwise(iterable):
    it = iter((*iterable, None))
    p = next(it)
    for i in it:
        yield p, i
        p = i


print(list(pairwise([])))
