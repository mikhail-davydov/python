import random


class RandomNumbers:
    def __init__(self, left, right, n):
        self.left = left
        self.right = right
        self.n = n

    def __next__(self):
        if self.n > 0:
            self.n -= 1
            return random.randint(self.left, self.right)
        raise StopIteration

    def __iter__(self):
        return self


iterator = RandomNumbers(1, 1, 3)

print(next(iterator))
print(next(iterator))
print(next(iterator))

# alt
from random import randint


class RandomNumbers:
    def __init__(self, left, right, n):
        self.data = (randint(left, right) for _ in range(n))

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.data)
