class FuzzyString(str):
    def __eq__(self, other):
        if not isinstance(other, str):
            return NotImplemented
        return self.__str__().lower().__eq__(other.__str__().lower())

    def __ne__(self, other):
        if not isinstance(other, str):
            return NotImplemented
        return self.__str__().lower().__ne__(other.__str__().lower())

    def __lt__(self, other):
        if not isinstance(other, str):
            return NotImplemented
        return self.__str__().lower().__lt__(other.__str__().lower())

    def __gt__(self, other):  # >
        if not isinstance(other, str):
            return NotImplemented
        return self.__str__().lower().__gt__(other.__str__().lower())

    def __le__(self, other):  # <=
        if not isinstance(other, str):
            return NotImplemented
        return self.__str__().lower().__le__(other.__str__().lower())

    def __ge__(self, other):  # >=
        if not isinstance(other, str):
            return NotImplemented
        return self.__str__().lower().__ge__(other.__str__().lower())

    def __contains__(self, other):  # other in self
        if not isinstance(other, str):
            return NotImplemented
        return self.__str__().lower().__contains__(other.__str__().lower())


# alt

class FuzzyString(str):
    def __new__(cls, obj):
        instance = super().__new__(cls, obj)
        for oper in map(lambda s: f'__{s}__', ('eq', 'ne', 'lt', 'le', 'gt', 'ge', 'contains')):
            setattr(cls, oper, cls._comparator(oper))
        return instance

    @staticmethod
    def _comparator(oper):
        def _compare(self, other):
            if not isinstance(other, (str, self.__class__)):
                return NotImplemented
            return getattr(self.lower(), oper)(other.lower())

        return _compare


# alt

def check(func):
    def wrapper(self, other):
        if isinstance(other, (str, FuzzyString)):
            return func(self, other)
        else:
            return NotImplemented

    return wrapper


class FuzzyString(str):
    @check
    def __eq__(self, other):
        return self.lower() == other.lower()

    @check
    def __ne__(self, other):
        return self.lower() != other.lower()

    @check
    def __lt__(self, other):
        return self.lower() < other.lower()

    @check
    def __le__(self, other):
        return self.lower() <= other.lower()

    @check
    def __gt__(self, other):
        return self.lower() > other.lower()

    @check
    def __ge__(self, other):
        return self.lower() >= other.lower()

    @check
    def __contains__(self, other):
        return other.lower() in self.lower()
