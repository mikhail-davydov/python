class Rectangle:
    def __init__(self, length, width):
        self.width = width
        self.length = length

    def __repr__(self):
        return f'Rectangle({self.length}, {self.width})'


rectangle = Rectangle(1, 2)

print(str(rectangle))
print(repr(rectangle))

print(10 * '-')

rectangle1 = Rectangle(1, 2)
rectangle2 = Rectangle(3, 4)

print(rectangle1)
print(repr(rectangle2))
