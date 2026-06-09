class QuadraticPolynomial:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @classmethod
    def from_iterable(cls, it):
        return cls(*it)

    @classmethod
    def from_str(cls, string):
        return cls.from_iterable((float(coef) for coef in string.split()))


polynom = QuadraticPolynomial(1, -5, 6)

print(polynom.a)
print(polynom.b)
print(polynom.c)

print(10 * '-')

polynom = QuadraticPolynomial.from_iterable([2, 13, -1])

print(polynom.a)
print(polynom.b)
print(polynom.c)

print(10 * '-')

polynom = QuadraticPolynomial(1, 2, -3)

polynom = QuadraticPolynomial.from_str('-1.5 4 14.8')

print(polynom.a)
print(polynom.b)
print(polynom.c)
print(polynom.a + polynom.b + polynom.c)
