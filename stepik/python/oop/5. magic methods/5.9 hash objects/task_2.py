from typing import Callable


def limited_hash(left: int, right: int, hash_function: Callable = hash) -> Callable:
    def new_hash(obj: object):
        hash_value = hash_function(obj)
        range_size = right - left + 1
        if left <= hash_value <= right:
            return hash_value
        if hash_value > right:
            return left + (hash_value - right - 1) % range_size
        if hash_value < left:
            return right - (left - hash_value - 1) % range_size

    return new_hash


# alt

def limited_hash(left, right, hash_function=hash):
    def inner_hash_function(x):
        return left + (hash_function(x) - left) % (right - left + 1)

    return inner_hash_function
