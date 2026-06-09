def first_true(iterable, predicate):
    return next(filter(predicate, iter(iterable)), None)


# alt
def first_true(iterable, predicate):
    if predicate is None:
        predicate = bool
    return next(dropwhile(lambda elem: not predicate(elem), iterable), None)


numbers = (0, 0, 0, 69, 1, 1, 1, 2, 4, 5, 6, 10, 100, 200)
print(first_true(numbers, None))

numbers = (0, 0, 0, 69, 1, 1, 1, 2, 4, 5, 6, 0, 10, 100, 200)
numbers_iter = filter(None, numbers)
