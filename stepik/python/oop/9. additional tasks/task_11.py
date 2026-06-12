import copy

import dataclasses


@dataclasses.dataclass
class Selfie:
    """
    Класс Selfie, экземпляры которого запоминают свои предыдущие состояния
    и умеют восстанавливаться до тех состояний, в которых они были раньше.
    Под состоянием объекта понимается определенный набор атрибутов и соответствующих значений.
    """
    _n_states: list = dataclasses.field(init=False, default_factory=list)

    def n_states(self):
        return len(self._n_states)

    def recover_state(self, n: int):
        try:
            return self._n_states[n]
        except IndexError:
            return self

    def save_state(self):
        current = copy.deepcopy(self)
        self._n_states.append(current)


# alt

import pickle
from itertools import count


class Selfie:
    def __init__(self):
        self._states = {}
        self._state = count()

    def save_state(self):
        self._states[next(self._state)] = pickle.dumps(self)

    def recover_state(self, n):
        obj = self._states.get(n)
        return pickle.loads(obj) if obj else self

    def n_states(self):
        return len(self._states)
