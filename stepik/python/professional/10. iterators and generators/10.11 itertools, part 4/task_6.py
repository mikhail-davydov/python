from itertools import groupby


def ranges(numbers):
    return list(map(lambda lst: (lst[0], lst[-1]),
                    [
                        list(group)
                        for _, group in groupby(numbers, key=lambda x: x - numbers.index(x))
                    ]
                    )
                )


# alt
def ranges(numbers):
    result = []
    for _, group in groupby(numbers, key=lambda n: n - numbers.index(n)):
        group = tuple(group)
        group = group[0], group[-1]
        result.append(group)
    return result


# alt
def ranges(a):
    c = groupby(a, key=lambda x: x - a.index(x))
    b = (tuple(v) for k, v in c)
    return [(i[0], i[-1]) for i in b]


numbers = [1, 2, 3, 4, 7, 8, 10]
print(ranges(numbers))

numbers = [1, 3, 5, 7]
print(ranges(numbers))

numbers = [1, 2, 3, 4, 5, 6, 7]
print(ranges(numbers))
