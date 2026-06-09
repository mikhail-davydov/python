class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_perimeter(self):
        return 2 * (self.width + self.length)

    def get_area(self):
        return self.width * self.length

    perimeter = property(get_perimeter)
    area = property(get_area)


rectangle = Rectangle(4, 5)

print(rectangle.length)
print(rectangle.width)
print(rectangle.perimeter)
print(rectangle.area)

print(10 * '-')

rectangle = Rectangle(4, 5)

rectangle.length = 2
rectangle.width = 3
print(rectangle.length)
print(rectangle.width)
print(rectangle.perimeter)
print(rectangle.area)
