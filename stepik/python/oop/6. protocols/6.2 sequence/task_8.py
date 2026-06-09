from copy import deepcopy

from typing import Iterable


class SequenceZip:
    def __init__(self, *iterables: list[Iterable]):
        self._data = deepcopy(zip(*iterables))

    def __len__(self):
        count = 0
        for _ in iter(deepcopy(self._data)):
            count += 1
        return count

    def __iter__(self):
        return iter(deepcopy(self._data))

    def __getitem__(self, index):
        data_copy = iter(deepcopy(self._data))
        while index > 0:
            next(data_copy)
            index -= 1
        return next(data_copy)


# alt

import copy


class SequenceZip:
    def __init__(self, *sequences):
        self.sequences = copy.deepcopy(sequences)

    def __len__(self):
        return min((len(s) for s in self.sequences), default=0)

    def __getitem__(self, index):
        count = -1
        for item in self:
            count += 1
            if count == index:
                return item

    def __iter__(self):
        yield from zip(*self.sequences)


# memory test

from memory_profiler import memory_usage


def func():
    many_large_sequences = [range(100000) for _ in range(100)]
    sequencezip = SequenceZip(*many_large_sequences)
    return sequencezip[99999]


if __name__ == '__main__':
    print(f"Peak usage: {max(memory_usage(func))}")
