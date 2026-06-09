class Counter:
    def __init__(self, start: int = 0):
        self.value = start

    def inc(self, n: int = 1):
        self.value += n

    def dec(self, n: int = 1):
        self.value = max(self.value - n, 0)


class DoubledCounter(Counter):
    def dec(self, n: int = 1):
        super().dec(n)
        super().dec(n)

    def inc(self, n: int = 1):
        super().inc(n)
        super().inc(n)
