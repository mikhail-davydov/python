from typing import Iterable


def intersperse(iterable: Iterable, delimiter: str):
    try:
        it = iter(iterable)
        yield next(it)
        for x in it:
            yield delimiter
            yield x
    except:
        return


# alt
def intersperse(iterable, delimiter):
    first = True
    for item in iterable:
        if not first:
            yield delimiter
        first = False
        yield item


# alt
def intersperse(iterable, delimiter):
    for i, v in enumerate(iterable):
        if i:
            yield delimiter
        yield v


print(*intersperse([1, 2, 3], 0))

inter = intersperse('beegeek', '!')
print(next(inter))
print(next(inter))
print(*inter)

print(*intersperse('A', '...'))
