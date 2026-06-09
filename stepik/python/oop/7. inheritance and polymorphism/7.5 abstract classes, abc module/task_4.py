from collections.abc import Iterable, Iterator


def is_iterable(obj):
    return isinstance(obj, Iterable)


def is_iterator(obj):
    return isinstance(obj, Iterator)
