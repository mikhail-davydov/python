import random


class Dice:
    def __init__(self, sides):
        self._sides = sides

    def __call__(self):
        return random.randint(1, self._sides)
