class RoundedInt(int):
    def __new__(cls, num: int, even: bool = True):
        if even and num % 2 == 1:
            num += 1
        if not even and num % 2 == 0:
            num += 1
        return super().__new__(cls, num)


# alt

class RoundedInt(int):
    def __new__(cls, value, even=True, *args, **kwargs):
        value += (value % 2 == 1) if even else (value % 2 == 0)
        instance = super().__new__(cls, value)
        return instance
