def success(login):
    print(f'Привет, {login}!')


def failure(login, text):
    print(f'{login}, попробуйте снова. Ошибка: {text}')


def verification(login, password, success, failure):
    if not any(c.isalpha() and c.isascii() for c in password):
        failure(login, 'в пароле нет ни одной буквы')
    elif not any(c.isupper() and c.isascii() for c in password):
        failure(login, 'в пароле нет ни одной заглавной буквы')
    elif not any(c.islower() and c.isascii() for c in password):
        failure(login, 'в пароле нет ни одной строчной буквы')
    elif not any(c.isdigit() and c.isascii() for c in password):
        failure(login, 'в пароле нет ни одной цифры')
    else:
        success(login)


verification('Arthur_Davletov', 'мойпароль123', success, failure)

# base
from string import ascii_letters, ascii_uppercase, ascii_lowercase, digits


def verification(login, password, success, failure):
    checks = [
        (lambda c: c in ascii_letters, 'в пароле нет ни одной буквы'),
        (lambda c: c in ascii_uppercase, 'в пароле нет ни одной заглавной буквы'),
        (lambda c: c in ascii_lowercase, 'в пароле нет ни одной строчной буквы'),
        (lambda c: c in digits, 'в пароле нет ни одной цифры'),
    ]

    for func, message in checks:
        if not any(map(func, password)):
            return failure(login, message)

    success(login)
