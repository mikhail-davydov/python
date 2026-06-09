def is_iterable(obj):
    return '__iter__' in dir(obj)


print(is_iterable('18731'))


# alt #1
def is_iterable(obj):
    return hasattr(obj, '__iter__')


# alt #2
from typing import Iterable


def is_iterable(obj):
    return isinstance(obj, Iterable)
