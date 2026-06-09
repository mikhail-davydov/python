def all_together(*args):
    return (i for it in args for i in it)


print(list(all_together()))

# alt
all_together = lambda *args: (x for iterable in args for x in iterable)


# alt
def all_together(*r):
    for i in r:
        yield from i
