def around(iterable):
    if not iterable:
        return

    it = iter(iterable)
    prev = None
    cur = next(it)

    for item in it:
        yield prev, cur, item
        prev, cur = cur, item

    yield prev, cur, None


# alt
def around(iterable):
    it = iter(iterable)
    chunk = (None, next(it, None), next(it, None))

    while not chunk[1] is None:
        yield chunk
        chunk = (*chunk[1:], next(it, None))


# alt # bad practice due to unpackaging
def around(iterable):
    it = tuple(iterable)
    yield from zip((None, *it), it, (*it[1:], None))


iterator = iter('hey')

print(*around(iterator))
