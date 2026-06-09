def takes_positive(func):
    def wrapper(*args, **kwargs):
        checks = [
            (lambda x: type(x) == int, TypeError),
            (lambda x: x > 0, ValueError),
        ]

        all_args = list(args) + list(kwargs.values())
        for f, error in checks:
            if not all(map(f, all_args)):
                raise error

        return func(*args, **kwargs)

    return wrapper


@takes_positive
def positive_sum(*args):
    return sum(args)


try:
    print(positive_sum('10', 20, 10))
except Exception as err:
    print(type(err))


# base
def takes_positive(func):
    def wrapper(*args, **kwargs):
        all_args = *args, *kwargs.values()

        if any([type(arg) != int for arg in all_args]):
            raise TypeError

        if any([arg <= 0 for arg in all_args]):
            raise ValueError

        return func(*args, **kwargs)

    return wrapper
