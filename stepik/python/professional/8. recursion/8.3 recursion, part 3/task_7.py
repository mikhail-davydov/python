def recursive_sum(a, b):
    if a == b == 0:
        return 0
    if a == 0:
        a, b = b, a
    return 1 + recursive_sum(a - 1, b)


print(recursive_sum(0, 0))


# base
def recursive_sum(a, b):
    if b == 0:
        return a
    return recursive_sum(a + 1, b - 1)
