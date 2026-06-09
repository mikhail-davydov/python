class Fibonacci:
    def __init__(self):
        self.a = 0
        self.b = 1
        self.n = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.n < 2:
            self.n += 1
            return 1
        value = self.a + self.b
        self.a, self.b, self.n = self.b, value, self.n + 1
        return value


fibonacci = Fibonacci()

print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))


# alt #1
class Fibonacci:
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a


# alt #2
from collections import deque


class Fibonacci:
    def __init__(self):
        self.nums = deque([0, 1], maxlen=2)

    def __iter__(self):
        return self

    def __next__(self):
        current = self.nums[-1]
        self.nums.append(sum(self.nums))
        return current
