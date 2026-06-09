from itertools import product


def password_gen():
    for item in product(range(10), repeat=3):
        yield ''.join(map(str, item))


# alt
def password_gen():
    for i, j, k in product(range(10), repeat=3):
        yield f'{i}{j}{k}'


passwords = password_gen()

print(next(passwords))
print(next(passwords))
print(next(passwords))
