from math import pi


class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.diameter = 2 * radius
        self.area = pi * radius ** 2


circle = Circle(5)

print(circle.radius)
print(circle.diameter)
print(circle.area)
