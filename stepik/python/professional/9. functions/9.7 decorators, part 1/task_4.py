def reverse_args(func):
    def wrapper(*args, **kwargs):
        return func(*reversed(args), **kwargs)
    return wrapper


@reverse_args
def concat(a, b, c):
    return a + b + c

print(concat('apple', 'cherry', 'melon'))