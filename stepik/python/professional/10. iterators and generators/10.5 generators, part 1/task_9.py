from collections.abc import Sequence


def flatten(nested_list):
    for elem in nested_list:
        if isinstance(elem, Sequence):
            yield from flatten(elem)
        else:
            yield elem


generator = flatten([1, 2, 3, 4, 5, 6, 7])

print(*generator)


# alt
def flatten(nested_list):
    for i in nested_list:
        yield from flatten(i) if isinstance(i, list) else [i]
