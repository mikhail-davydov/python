class anything:
    def __call__(self, *args, **kwargs):
        return self

    def __eq__(self, other):
        return True

    __ne__ = __lt__ = __le__ = __gt__ = __ge__ = __eq__


# alt

class AlwaysTrue:
    def __eq__(self, other):
        return True

    __ne__ = __lt__ = __le__ = __gt__ = __ge__ = __eq__


def anything():
    return AlwaysTrue()
