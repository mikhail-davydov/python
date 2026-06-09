from functools import lru_cache


@lru_cache
def ways(n):
    if n == 1:
        return 1
    if n < 1:
        return 0
    return ways(n - 1) + ways(n - 3) + ways(n - 4)


# alt
def ways(n):
    way = [0, 1, 1, 1, 2] + [0] * (n - 1)
    for i in range(5, n + 1):
        way[i] = way[i - 1] + way[i - 3] + way[i - 4]
    return way[n]
