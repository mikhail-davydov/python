import itertools

n = int(input())
m = int(input())

if n <= 10:
    digits = [str(i) for i in range(n)]
else:
    digits = [str(i) for i in range(10)]
    digits.extend([chr(ord('A') + i) for i in range(n - 10)])

combinations = itertools.product(digits, repeat=m)

numbers = [''.join(combo) for combo in combinations]

print(' '.join(numbers))

# alt
import itertools as it
from string import ascii_uppercase, digits

n, m = int(input()), int(input())
symbols = (digits + ascii_uppercase)[:n]

print(*map("".join, it.product(symbols, repeat=m)))
