import sys

from contextlib import contextmanager


@contextmanager
def reversed_print():
    temp = sys.stdout.write
    sys.stdout.write = lambda text: temp(text[::-1])
    yield
    sys.stdout.write = temp


# alt

@contextmanager
def reversed_print():
    original_write = sys.stdout.write

    def reverse_write(text):
        original_write(text[::-1])

    sys.stdout.write = reverse_write
    yield
    sys.stdout.write = original_write
