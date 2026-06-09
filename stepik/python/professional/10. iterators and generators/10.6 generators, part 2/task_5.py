def interleave(*args):
    return (i for elem in zip(*args) for i in elem)


numbers = [1, 2, 3]
squares = [1, 4, 9]
qubes = [1, 8, 27]

print(*interleave(numbers, squares, qubes))


# alt
def interleave(*args):
    for iterable in zip(*args):
        yield from iterable


# alt
interleave = lambda *x: (j for i in zip(*x) for j in i)
