class predicate:
    """
    Декоратор, который позволяет удобно комбинировать предикаты с помощью операторов &, | и ~

    Пример:

    @predicate
    def is_even(num):
        return num % 2 == 0

    @predicate
    def is_positive(num):
        return num > 0

    print((is_even & is_positive)(4))             # True; равнозначно is_even(4) and is_positive(4)
    print((is_even & is_positive)(3))             # False; равнозначно is_even(3) and is_positive(3)
    print((is_even | is_positive)(3))             # True; равнозначно is_even(3) or is_positive(3)
    print((~is_even & is_positive)(3))            # True; равнозначно not is_even(3) and is_positive(3)
    """

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)

    def __and__(self, other):
        return predicate(lambda *args, **kwargs: self(*args, **kwargs) and other(*args, **kwargs))

    def __or__(self, other):
        return predicate(lambda *args, **kwargs: self(*args, **kwargs) or other(*args, **kwargs))

    def __invert__(self):
        return predicate(lambda *args, **kwargs: not self(*args, **kwargs))


# alt

class predicate:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)

    def __invert__(self):
        def not_func(*args, **kwargs):
            return not self.func(*args, **kwargs)

        return type(self)(not_func)

    def __or__(self, other):
        def or_func(*args, **kwargs):
            return self.func(*args, **kwargs) or other.func(*args, **kwargs)

        return type(self)(or_func)

    def __and__(self, other):
        def and_func(*args, **kwargs):
            return self.func(*args, **kwargs) and other.func(*args, **kwargs)

        return type(self)(and_func)
