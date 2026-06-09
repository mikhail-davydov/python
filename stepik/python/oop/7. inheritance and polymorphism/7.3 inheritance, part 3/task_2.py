class LowerString(str):
    def __new__(cls, *args, **kwargs):
        obj = args[0] if args else ''
        return super().__new__(cls, str(obj).lower())


# alt

class LowerString(str):
    def __new__(cls, string=''):
        instance = super().__new__(cls, str(string).lower())
        return instance
