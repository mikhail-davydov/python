class ArithmeticProgression:
    def __init__(self, first, diff):
        self.first = first
        self.diff = diff

    def __iter__(self):
        return self

    def __next__(self):
        result = self.first
        self.first += self.diff
        return result


class GeometricProgression:
    def __init__(self, first, mult):
        self.first = first
        self.mult = mult

    def __iter__(self):
        return self

    def __next__(self):
        result = self.first
        self.first *= self.mult
        return result


# alt

from abc import ABC, abstractmethod


class Progression(ABC):
    def __init__(self, start, step):
        self._current = start
        self._step = step

    def __iter__(self):
        return self

    @abstractmethod
    def __next__(self):
        pass


class ArithmeticProgression(Progression):
    def __next__(self):
        answer = self._current
        self._current += self._step
        return answer


class GeometricProgression(Progression):
    def __next__(self):
        answer = self._current
        self._current *= self._step
        return answer
