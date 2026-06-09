def get_fast_pow(a, n):
    def even(a, n):
        return get_fast_pow(a, n)

    def odd(a, n):
        return get_fast_pow(a, n)

    if n == 0:
        return 1
    return even(a * a, n / 2) if n % 2 == 0 else a * odd(a, n - 1)


print(get_fast_pow(2, 100))


# base solution
def get_fast_pow(number, power):
    if power == 0:
        return 1
    elif power % 2:
        return number * get_fast_pow(number, power - 1)
    return get_fast_pow(number * number, power // 2)
