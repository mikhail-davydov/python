class Counter:
    def __init__(self, start: int = 0):
        self.value = start

    def inc(self, n: int = 1):
        self.value += n

    def dec(self, n: int = 1):
        self.value = 0 if n > self.value else self.value - n

    # alt
    # def dec(self, n=1):
    #     self.value = max(self.value - n, 0)


class NonDecCounter(Counter):
    def dec(self, n: int = 1):
        pass


class LimitedCounter(Counter):
    def __init__(self, start: int = 0, limit: int = 10):
        super().__init__(start)
        self.limit = limit

    def inc(self, n: int = 1):
        super().inc(n)
        self.value = self.value if self.value < self.limit else self.limit

    # alt
    # def inc(self, n=1):
    #     self.value = min(self.value + n, self.limit)
