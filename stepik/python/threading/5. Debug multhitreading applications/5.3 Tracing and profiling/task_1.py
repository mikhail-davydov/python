import sys
from operator import truediv

c_calls: list[str] = []


def profile_func(frame, event, arg):
    if event == 'c_call':
        c_calls.append(arg.__name__)


sys.setprofile(profile_func)


def divide(a, b):
    return truediv(a, b)  # <-!


if __name__ == '__main__':
    divide(4, 2)
    print(c_calls)
