def random_numbers(left, right):
    return iter(lambda: random.randint(left, right), 0)


iterator = random_numbers(1, 10)

print(next(iterator) in range(1, 11))
print(next(iterator) in range(1, 11))
print(next(iterator) in range(1, 11))

# alt #1
from random import randint


def random_numbers(left, right):
    def get_random_number():
        return randint(left, right)

    return iter(get_random_number, right + 1)


# alt #2
import random


class random_numbers:

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __next__(self):
        return random.randint(self.left, self.right)

    def __iter__(self):
        return self
