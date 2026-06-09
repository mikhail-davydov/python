def alternating_sequence(count=None):
    sign = (-1, 1)
    if count:
        yield from (i * sign[i % 2] for i in range(1, count + 1))
    else:
        value = 1
        while True:
            yield value * sign[value % 2]
            value += 1


generator = alternating_sequence()

print(next(generator))
print(next(generator))


# alt
def alternating_sequence(count=None):
    n = 0
    while n != count:
        n += 1
        yield n if n % 2 else -n
        