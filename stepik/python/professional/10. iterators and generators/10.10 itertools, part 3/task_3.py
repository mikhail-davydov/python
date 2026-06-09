from itertools import pairwise


def max_pair(iterable):
    pair_sum = 0
    for a, b in pairwise(iterable):
        if (a + b) > pair_sum:
            pair_sum = a + b
    return pair_sum


# alt
def max_pair(iterable):
    return max(map(sum, pairwise(iterable)))


print(max_pair([1, 8, 2, 4, 3]))

iterator = iter([1, 2, 3, 4, 5])
print(max_pair(iterator))

iterator = iter([0, 0, 0, 0, 0, 0, 0, 0, 0])
print(max_pair(iterator))
