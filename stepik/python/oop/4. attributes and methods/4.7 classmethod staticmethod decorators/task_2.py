class Rectangle:

    def __init__(self, length, width):
        self.width = width
        self.length = length

    @classmethod
    def square(cls, side):
        return cls(side, side)


rectangle = Rectangle(4, 5)

print(rectangle.length)
print(rectangle.width)

print(10 * '-')

rectangle = Rectangle.square(5)

print(rectangle.length)
print(rectangle.width)
