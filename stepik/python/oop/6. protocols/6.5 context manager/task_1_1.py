def is_context_manager(obj: object):
    return all(method in obj.__dir__() for method in ('__enter__', '__exit__'))


# alt

def is_context_manager(obj):
    return hasattr(obj, '__enter__') and hasattr(obj, '__exit__')
