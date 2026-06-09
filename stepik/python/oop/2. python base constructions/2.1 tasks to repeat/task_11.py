import re
from fractions import Fraction


def is_fraction(string):
    if not string:
        return False
    regex_obj = re.compile(r'-?\d+/\d*[1-9]+\d*')
    return bool(regex_obj.fullmatch(string))


# alt
def is_fraction(string):
    try:
        Fraction(string)
        return '/' in string
    except (ValueError, ZeroDivisionError):
        return False


print(is_fraction('1000/1'))
print(is_fraction('-54/9'))
print(is_fraction('71'))
print(is_fraction('1/0'))
print(is_fraction(''))
