import functools


def limiter(limit: int, unique: str, lookup: str):
    def decorator(cls):
        cls._INSTANCES = []

        def wrapper(*args, **kwargs):
            instance = cls(*args, **kwargs)

            for current in cls._INSTANCES:
                if getattr(current, unique) == getattr(instance, unique):
                    return current

            if len(cls._INSTANCES) < limit:
                cls._INSTANCES.append(instance)
                return instance

            match lookup:
                case 'FIRST':
                    return cls._INSTANCES[0]
                case 'LAST':
                    return cls._INSTANCES[-1]
                case _:
                    raise ValueError(f'Unknown lookup value: {lookup}')

        return wrapper

    return decorator


# alt

class limiter:

    def __init__(self, limit: int, unique: str, lookup: str):
        self.limit = limit
        self.unique = unique
        self.lookup = lookup

    def __call__(self, cls):
        cls._INSTANCES = []

        new_origin = cls.__new__
        init_origin = cls.__init__

        @functools.wraps(new_origin)
        def __new__(cls, *args, **kwargs):
            instance = new_origin(cls)
            init_origin(instance, *args, **kwargs)

            for current in cls._INSTANCES:
                if getattr(current, self.unique) == getattr(instance, self.unique):
                    return current

            if len(cls._INSTANCES) < self.limit:
                cls._INSTANCES.append(instance)
                return instance

            match self.lookup:
                case 'FIRST':
                    return cls._INSTANCES[0]
                case 'LAST':
                    return cls._INSTANCES[-1]
                case _:
                    raise ValueError(f'Unknown lookup value: {self.lookup}')

        @functools.wraps(init_origin)
        def __init__(self, *args, **kwargs):
            pass

        cls.__new__ = __new__
        cls.__init__ = __init__

        return cls
