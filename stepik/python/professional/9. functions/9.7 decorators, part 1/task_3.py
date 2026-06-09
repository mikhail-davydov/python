def do_twice(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)

    return wrapper


@do_twice
def beegeek():
    print('beegeek')


print(beegeek())


# alt
def do_twice(fun):
    return lambda *args, **kwargs: [fun(*args, **kwargs), fun(*args, **kwargs)][1]
