import re
from typing import Any


class CCD:
    def __init__(self, data: dict):
        self.cat: str = data['cat']
        self.union: bool = data['union']
        self.cargo: Any = data['cargo']
        self.id: int = data['id']

    # alt
    # def __init__(self, kwargs):
    #     self.__dict__.update(**kwargs)

    def __lt__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self._priority() < other._priority()

    def _priority(self):
        cat_priority = True if re.fullmatch(r'020.', self.cat) else False
        return ~int(self.union), ~int(cat_priority), self.id
        # return not self.union, not cat_priority, self.id


d1 = {"cat": "0210", "union": True, "cargo": {"stew", 2}, "id": 1}
d2 = {"cat": "0208", "union": True, "cargo": {"liver", 1.78}, "id": 2}
d3 = {"cat": "0208", "union": True, "cargo": {"liver", 56}, "id": 3}
d4 = {"cat": "0209", "union": False, "cargo": {"pork fat", 100}, "id": 4}
d5 = {"cat": "87", "union": False, "cargo": {"bombardier", 1}, "id": 5}
d6 = {"cat": "0201", "union": False, "cargo": {"veal", 120}, "id": 7}
d7 = {"cat": "0201", "union": False, "cargo": {"veal", 79}, "id": 6}

dataset = [CCD(d) for d in (d1, d2, d3, d4, d5, d6, d7)]
print(*(ccd.id for ccd in sorted(dataset)))

# Если класс CCD реализован правильно, то отсортированный список id деклараций будет распечатан так:
# 2 3 1 4 6 7 5
