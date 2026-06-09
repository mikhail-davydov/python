class ColoredPoint:
    def __init__(self, x, y, color):
        self._x = x
        self._y = y
        self._color = color

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def color(self):
        return self._color

    def __repr__(self):
        return f'{self.__class__.__name__}{(self._x, self._y, self._color)!r}'

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return all([
            self._x == other._x,
            self._y == other._y,
            self._color == other._color
        ])

    def __hash__(self):
        return hash((self._x, self._y, self._color))
