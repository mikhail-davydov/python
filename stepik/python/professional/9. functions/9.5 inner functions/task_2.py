def generator_square_polynom(a, b, c):
    return lambda x: a * x ** 2 + b * x + c


f = generator_square_polynom(26, 83, 22)
print(f(55))


# alt
def generator_square_polynom(a, b, c):
    def inner(x):
        return a * x ** 2 + b * x + c

    return inner
