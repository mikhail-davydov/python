def check_type(func):
    def wrapper(self, other):
        if hasattr(other, '__iter__'):
            return func(self, other)
        else:
            return NotImplemented

    return wrapper


class AdvancedTuple(tuple):
    @check_type
    def __add__(self, other):
        return self.__class__(list(self) + list(other))

    @check_type
    def __radd__(self, other):
        return self.__class__(list(other) + list(self))


# alt

class AdvancedTuple(tuple):
    def __add__(self, other):
        if hasattr(other, '__iter__'):
            return AdvancedTuple(tuple(self) + tuple(other))
        return NotImplemented

    def __radd__(self, other):
        if hasattr(other, '__iter__'):
            return AdvancedTuple(tuple(other) + tuple(self))
        return NotImplemented

    def __iadd__(self, other):
        if hasattr(other, '__iter__'):
            return AdvancedTuple(tuple(self) + tuple(other))
        return NotImplemented
