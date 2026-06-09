class PasswordError(Exception):
    pass


class LengthError(PasswordError):
    pass


class LetterError(PasswordError):
    pass


class DigitError(PasswordError):
    pass


def is_good_password(st: str) -> bool:
    if len(st) < 9:
        raise LengthError
    if not any(c.isupper() for c in st) or not any(c.islower() for c in st):
        raise LetterError
    if not any(c.isdigit() for c in st):
        raise DigitError
    return True


try:
    print(is_good_password('41157081231232'))
except Exception as err:
    print(type(err))


# alternative solution
class PasswordError(Exception):    ...


class LengthError(PasswordError):    ...


class LetterError(PasswordError):    ...


class DigitError(PasswordError):  ...


def myraise(err):   raise err


def is_good_password(string: str) -> bool:
    len(string) >= 9 or myraise(LengthError)
    string != string.upper() and string != string.lower() or myraise(LetterError)
    any(i in string for i in '0123456789') or myraise(DigitError)
    return True
