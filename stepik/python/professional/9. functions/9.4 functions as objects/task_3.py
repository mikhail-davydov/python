def polynom(x):
    result = x ** 2 + 1
    if 'values' not in polynom.__dict__:
        polynom.values = set()
    polynom.values.add(result)
    return result


polynom(1)
polynom(2)
polynom(3)

print(*sorted(polynom.values))


# base
def polynom(x):
    polynom.__dict__.setdefault('values', set())
    value = x ** 2 + 1
    polynom.values.add(value)
    return value
