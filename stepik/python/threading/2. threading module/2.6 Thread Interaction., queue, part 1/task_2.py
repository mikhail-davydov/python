import queue
from collections.abc import Generator


def get_obj() -> Generator:
    pass


def is_prime(elem):
    pass


prime_queue = queue.Queue()
sub_queue = queue.Queue()

for elem in get_obj():
    prime_queue.put(elem) if is_prime(elem) else sub_queue.put(elem)
