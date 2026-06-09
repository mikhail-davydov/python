class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Вектор на плоскости с координатами ({self.x}, {self.y})'

    def __repr__(self):
        return f'Vector({self.x}, {self.y})'


# alt
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Вектор на плоскости с координатами ({self.x}, {self.y})'

    def __repr__(self):
        class_name = type(self).__name__
        return f'{class_name}({self.x}, {self.y})'


vector = Vector(1, 2)

print(str(vector))
print(repr(vector))

print(10 * '-')

vectors = [Vector(1, 2), Vector(3, 4)]

print(vectors)
