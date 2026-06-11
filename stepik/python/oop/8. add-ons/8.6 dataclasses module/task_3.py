from dataclasses import dataclass, field


@dataclass
class Point:
    x: float = 0.0
    y: float = 0.0
    quadrant: int = field(init=False, compare=False)

    def symmetric_x(self):
        return Point(self.x, -self.y)

    def symmetric_y(self):
        return Point(-self.x, self.y)

    def __post_init__(self):
        if self.x > 0 and self.y > 0:
            self.quadrant = 1
        elif self.x < 0 and self.y > 0:
            self.quadrant = 2
        elif self.x < 0 and self.y < 0:
            self.quadrant = 3
        elif self.x > 0 and self.y < 0:
            self.quadrant = 4
        else:
            self.quadrant = 0


# alt

@dataclass
class Point:
    x: float = 0.0
    y: float = 0.0
    quadrant: int = field(default=0, compare=False)

    def __post_init__(self):
        if self.x > 0 and self.y != 0:
            self.quadrant = (1, 4)[self.y < 0]
        elif self.x < 0 and self.y != 0:
            self.quadrant = (2, 3)[self.y < 0]

    def symmetric_x(self):
        return type(self)(self.x, -self.y)

    def symmetric_y(self):
        return type(self)(-self.x, self.y)


# alt

@dataclass
class Point:
    x: float = 0.0
    y: float = 0.0
    quadrant: int = field(init=False)

    def __post_init__(self):
        self.quadrant = {
            self.x > 0 and self.y > 0: 1,
            self.x > 0 and self.y < 0: 4,
            self.x < 0 and self.y < 0: 3,
            self.x < 0 and self.y > 0: 2}.get(True, 0)

    def symmetric_x(self):
        return self.__class__(self.x, -self.y)

    def symmetric_y(self):
        return self.__class__(-self.x, self.y)
