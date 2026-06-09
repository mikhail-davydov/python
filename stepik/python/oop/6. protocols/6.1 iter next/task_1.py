class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self._cords = self.x, self.y, self.z

    def __repr__(self):
        return f'{__class__.__name__}{self._cords!r}'

    # def __iter__(self):
    #     return iter(self._cords)

    def __iter__(self):
        yield from self._cords
