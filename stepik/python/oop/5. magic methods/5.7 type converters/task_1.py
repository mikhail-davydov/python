class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __abs__(self):
        return (pow(self.x, 2) + pow(self.y, 2)) ** 0.5

    def __str__(self):
        return f'{self.x, self.y}'

    def __bool__(self):
        return any([self.x, self.y])

    def __int__(self):
        return int(abs(self))

    def __float__(self):
        return abs(self)

    def __complex__(self):
        return complex(self.x, self.y)
