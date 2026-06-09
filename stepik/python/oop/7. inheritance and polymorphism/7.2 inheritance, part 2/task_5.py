class Summator:
    def __init__(self):
        self.sum_dict = {1: 1}
        self.m = 1

    def total(self, n: int):
        if n in self.sum_dict:
            return self.sum_dict[n]
        self.sum_dict[n] = n ** self.m + self.total(n - 1)
        return self.sum_dict[n]


class SquareSummator(Summator):

    def __init__(self):
        super().__init__()
        self.m = 2


class QubeSummator(Summator):

    def __init__(self):
        super().__init__()
        self.m = 3


class CustomSummator(Summator):
    def __init__(self, m):
        super().__init__()
        self.m = m


# alt

class Summator:
    base = 1

    def total(self, n: int):
        return sum(it ** self.base for it in range(1, n + 1))


class SquareSummator(Summator):
    base = 2


class QubeSummator(Summator):
    base = 3


class CustomSummator(Summator):
    def __init__(self, base):
        self.base = base
