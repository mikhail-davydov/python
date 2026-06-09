def tribonacci(n):
    trb_nums = {1: 1, 2: 1, 3: 1}

    def _inner(n):
        if n in trb_nums:
            return trb_nums[n]
        result = _inner(n - 1) + _inner(n - 2) + _inner(n - 3)
        trb_nums[n] = result
        return result

    return _inner(n)


print(tribonacci(7))


# base
def tribonacci(n):
    cache = {1: 1, 2: 1, 3: 1}

    def rec(n):
        if n not in cache:
            cache[n] = rec(n - 3) + rec(n - 2) + rec(n - 1)
        return cache[n]

    return rec(n)
