def map(function, items):
    return [function(item) for item in items]


def filter(function, items):
    return [item for item in items if function(item)]


def reduce(function, items, initial=None):
    if initial is None:
        initial = items[0]
        items = items[1:]

    total_value = initial
    for item in items:
        total_value = function(total_value, item ** 2)
    return total_value


def sum(a, b):
    return a + b


def predicate(x):
    return 1 if len(str(abs(x))) == 2 and x % 7 == 0 else 0


numbers = [7, -6, 23, 287, -147, -26, 3]

print(reduce(sum, filter(predicate, numbers), 0))
