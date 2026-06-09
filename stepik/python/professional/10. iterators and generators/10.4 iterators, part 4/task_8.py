class Cycle:
    def __init__(self, iterable):
        self.iterable = iterable
        self.iterator = iter(self.iterable)

    def __next__(self):
        try:
            return next(self.iterator)
        except StopIteration:
            self.iterator = iter(self.iterable)
            return next(self.iterator)

    def __iter__(self):
        return self


cycle = Cycle('be')

print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))


# alt
class Cycle:
    def __init__(self, iterable):
        self.iterable = iterable
        self.index = 0
        self.length = len(iterable)

    def __iter__(self):
        return self

    def __next__(self):
        item = self.iterable[self.index]
        self.index = (self.index + 1) % self.length
        return item
