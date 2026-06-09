def is_power(power) -> bool:
    if power in [1, 2]:
        return True
    if power < 2:
        return False
    return is_power(power / 2)


print(is_power(15))


# base
def is_power(number):
    if number <= 2:
        return True
    elif number % 2:
        return False
    return is_power(number // 2)


# alt
def is_power(n):
    if n % 2 != 0:
        return n == 1
    return is_power(n // 2)
