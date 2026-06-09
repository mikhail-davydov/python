import re


def is_integer(param):
    try:
        num = int(param)
        return True
    except:
        return False


# alt
def is_integer(string: str) -> bool:
    regex_obj = re.compile(r'-?\d+')
    return bool(regex_obj.fullmatch(string))


print(is_integer('199'))
print(is_integer('-43'))
print(is_integer('5f'))
print(is_integer('5.0'))
print(is_integer('1.1'))
