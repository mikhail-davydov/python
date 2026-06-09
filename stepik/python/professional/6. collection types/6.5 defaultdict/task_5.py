def flip_dict(dict_of_lists):
    flipped = defaultdict(list)
    for key, values in dict_of_lists.items():
        for value in values:
            flipped[value].append(key)
    return flipped


print(flip_dict({'a': [1, 2], 'b': [3, 1], 'c': [2]}))

# alternative solution
from collections import defaultdict


def flip_dict(
        dict_of_lists: dict[str | int, list[str | int]]
) -> defaultdict[str | int, list[str | int]]:
    result = defaultdict(list)
    [result[v].append(k) for k, v_list in dict_of_lists.items() for v in v_list]

    return result
