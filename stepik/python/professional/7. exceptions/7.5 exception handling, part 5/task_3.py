class PasswordError(Exception):
    ...


class LengthError(PasswordError):
    ...


class LetterError(PasswordError):
    ...


class DigitError(PasswordError):
    ...


def myraise(err):   raise err


def is_good_password(string: str) -> bool:
    len(string) >= 9 or myraise(LengthError)
    string != string.upper() and string != string.lower() or myraise(LetterError)
    any(i in string for i in '0123456789') or myraise(DigitError)
    return True


good_pass = False
while not good_pass:
    try:
        good_pass = is_good_password(input().strip())
    except PasswordError as err:
        print(err.__class__.__name__)

print('Success!')
