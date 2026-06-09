class Xrange:
    def __init__(self, start: int | float, end: int | float, step: int | float = 1):
        self.start = start
        self.end = end
        self.step = step

    def __next__(self):
        conditions = (
            not self.step,
            self.step > 0 and self.start >= self.end,
            self.step < 0 and self.start <= self.end,
        )
        if any(conditions):
            raise StopIteration
        current = self.start
        self.start += self.step
        return float(current) if any(isinstance(x, float) for x in (self.start, self.step, self.step)) else current

    def __iter__(self):
        return self


xrange = Xrange(0, 3, 0.5)

print(*xrange, sep='; ')


# alt
class Xrange:
    def __init__(self, start, end, step=1):
        self.start = start - step
        self.end = end
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if abs(self.end - self.start) <= abs(self.step):
            raise StopIteration
        self.start += self.step
        return self.start
