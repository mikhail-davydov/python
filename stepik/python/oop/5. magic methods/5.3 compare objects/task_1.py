class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        if isinstance(other, tuple):
            x, y, *rest = other
            return not rest and self.x == x and self.y == y
        return NotImplemented

    def __repr__(self):
        class_name = self.__class__.__name__
        return f'{class_name}({self.x}, {self.y})'


# alt
class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    @property
    def fields(self):
        return self.x, self.y

    def __repr__(self):
        return f'Vector({self.x}, {self.y})'

    def __eq__(self, other):
        if isinstance(other, Vector):
            return self.fields == other.fields
        if isinstance(other, tuple):
            return self.fields == other
        return NotImplemented


a = Vector(1, 2)
b = Vector(1, 2)

print(a == b)
print(a != b)

print(10 * '-')

a = Vector(1, 2)
pair1 = (1, 2)
pair2 = (3, 4)
pair3 = (5, 6, 7)
pair4 = (1, 2, 3, 4)
pair5 = (1, 4, 3, 2)

print(a == pair1)
print(a == pair2)
print(a == pair3)
print(a == pair4)
print(a == pair5)
