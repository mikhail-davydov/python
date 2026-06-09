def is_palindrome(text):
    return text == text[::-1]


def generate_palindrom():
    idx = 1
    while idx:
        if is_palindrome(str(idx)):
            yield idx
        idx += 1


def palindromes():
    yield from generate_palindrom()


generator = palindromes()
numbers = [next(generator) for _ in range(30)]

print(*numbers)


# alt
def palindromes():
    yield from (i for i, _ in enumerate(iter(bool, True), 1) if str(i) == str(i)[::-1])


# alt
def palindromes():
    def nums_gen(count=1):
        while True:
            if str(count) == str(count)[::-1]:
                yield count
            count = count + 1

    yield from nums_gen()


# alt
'''
решение основано на собирании палиндрома из строк
'''
from string import digits


def palindromes():
    def pali(n):  # Внутренний генератор "строковых" палиндромов длиной n
        if n == 1:
            yield from digits
        elif n == 2:
            yield from (d * 2 for d in digits)
        else:  # Рекурсивный случай - "оборачиваем" одинаковыми цифрами "внутренние палиндромы"
            yield from (f"{d}{p}{d}" for d in digits for p in pali(n - 2))

    i = 0
    while True:
        i += 1
        for x in pali(i):  # Получаем все значения из внутреннего генератора
            if x[0] != "0":  # Если значение начинается с "0", оно недопустимо
                yield int(x)
