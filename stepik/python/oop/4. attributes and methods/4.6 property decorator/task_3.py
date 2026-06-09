class QuadraticPolynomial:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @property
    def x1(self):
        if self.__has_roots() < 0:
            return None
        return (-self.b - self.__has_roots() ** 0.5) / (2 * self.a)

    @property
    def x2(self):
        if self.__has_roots() < 0:
            return None
        return (-self.b + self.__has_roots() ** 0.5) / (2 * self.a)

    @property
    def view(self):
        sign_b = '+' if self.b >= 0 else '-'
        sign_c = '+' if self.c >= 0 else '-'
        return f'{self.a}x^2 {sign_b} {abs(self.b)}x {sign_c} {abs(self.c)}'

    @property
    def coefficients(self):
        return self.a, self.b, self.c

    @coefficients.setter
    def coefficients(self, value):
        self.a, self.b, self.c = value

    def __has_roots(self):
        return self.b ** 2 - 4 * self.a * self.c


polynom = QuadraticPolynomial(1, 2, -3)

print(polynom.a)
print(polynom.b)
print(polynom.c)

print(10 * '-')

polynom = QuadraticPolynomial(1, 2, -3)

print(polynom.x1)
print(polynom.x2)

print(10 * '-')

polynom = QuadraticPolynomial(1, 2, -3)

print(polynom.view)
print(polynom.coefficients)

print(10 * '-')

polynom = QuadraticPolynomial(1, 2, -3)

polynom.coefficients = (1, -5, 6)
print(polynom.x1)
print(polynom.x2)
print(polynom.view)
