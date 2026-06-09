from itertools import dropwhile


def drop_this(numbers, obj):
    return dropwhile(lambda x: x == obj, numbers)


iterator = iter('bbbbeebee')

print(*drop_this(iterator, 'b'))
