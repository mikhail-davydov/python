def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False
    return True


def primes(left, right):
    yield from filter(is_prime, range(left, right + 1))


generator = primes(6, 36)

print(next(generator))
print(next(generator))

# alt
from typing import Generator


def primes(left: int, right: int) -> Generator:
    sieve = [False] * 2 + [True] * (right - 1)
    for i in range(2, right):
        if sieve[i]:
            for j in range(i * 2, right + 1, i):
                sieve[j] = False
    return (digit for digit, value in enumerate(sieve) if value and digit >= left)


# alt #2
from math import sqrt


def primes(left, right):
    left = max(2, left)
    for num in range(left, right + 1):
        if all(map(lambda x: num % x != 0, range(2, int(sqrt(num)) + 1))):
            yield num
