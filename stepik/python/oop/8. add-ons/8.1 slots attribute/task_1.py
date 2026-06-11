import functools


@functools.total_ordering
class Shape:
    __slots__ = ('name', 'color', 'area')

    def __init__(self, name, color, area):
        self.name = name
        self.color = color
        self.area = area

    def __str__(self):
        return f'{self.color} {self.name} ({self.area})'

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self.area == other.area

    def __lt__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self.area < other.area
