from itertools import dropwhile


def drop_while_negative(numbers):
    return dropwhile(lambda x: x < 0, numbers)


iterator = iter([-3, -2, -1, 0, 1, 2, 3, -4, -5, -6])

print(*drop_while_negative(iterator))
