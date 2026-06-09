def is_prime(number):
    return number != 1 and all(number % i != 0 for i in range(2, number))


print(is_prime(7))


# alt
def is_prime(number):
    if number != 1:
        return all(number % i != 0 for i in range(2, int(number ** 0.5) + 1))
    return False
