import string

from itertools import cycle


def alnum_sequence():
    lst = list()
    for item in enumerate(string.ascii_uppercase, 1):
        lst.extend(item)
    return cycle(lst)


# alt
def alnum_sequence():
    return cycle(elem for alnum_tuple in enumerate(string.ascii_uppercase, 1) for elem in alnum_tuple)


# alt
def alnum_sequence():
    for item in zip(cycle(range(1, 27)), cycle(string.ascii_uppercase)):
        yield from item


alnum = alnum_sequence()

print(*(next(alnum) for _ in range(100)))
