def simple_sequence():
    value = 1
    index = 1
    while index:
        yield value
        index -= 1
        if not index:
            value += 1
            index = value


generator = simple_sequence()
numbers = [next(generator) for _ in range(10)]

print(*numbers)


# alt
def simple_sequence():
    number = 1
    while True:
        for _ in range(number):
            yield number
        number += 1


# alt
def simple_sequence():
    count = 1

    while True:
        yield from (count for _ in range(count))
        count += 1
