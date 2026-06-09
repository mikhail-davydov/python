def count_iterable(iterable):
    return sum(1 for _ in iterable)


data = tuple(range(432, 3845, 17))

print(count_iterable(data))
