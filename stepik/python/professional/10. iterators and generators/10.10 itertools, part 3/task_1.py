from itertools import chain


def sum_of_digits(iterable):
    total = 0
    for elem in iterable:
        # total += sum(map(int, str(elem)))
        total += sum(chain(map(int, str(elem))))
    return total


# alt
def sum_of_digits(iterable):
    strings = map(str, iterable)
    all_elements = chain.from_iterable(strings)
    int_digits = map(int, all_elements)
    return sum(int_digits)


print(sum_of_digits([13, 20, 41, 2, 2, 5]))
print(sum_of_digits((1, 2, 3, 4, 5, 6, 7, 8, 9, 10)))
print(sum_of_digits([123456789]))
