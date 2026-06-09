from itertools import compress, count


def first_largest(iterable, number):
    try:
        return next(filter(lambda x: x[1] > number, enumerate(iterable)))[0]
    except:
        return -1


# alt
def first_largest(iterable, number):
    return next(compress(count(), (i > number for i in iterable)), -1)


numbers = [10, 2, 14, 7, 7, 18, 20]
print(first_largest(numbers, 11))

iterator = iter([-1, -2, -3, -4, -5])
print(first_largest(iterator, 10))

iterator = iter([18, 21, 14, 72, 73, 18, 20])
print(first_largest(iterator, 10))
