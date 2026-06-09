import builtins


def custom_print(*args, sep=' ', end='\n'):
    args = (arg.upper() if type(arg) == str else arg for arg in args)
    sep = sep.upper()
    end = end.upper()
    builtins.print(*args, sep=sep, end=end)


print = custom_print

print('beegeek', [1, 2, 3], 4)
print('bee', 'geek', sep=' and ', end=' wow')

# base
builtin_print = print


def print(*args, sep=' ', end='\n'):
    args = [str(arg).upper() if isinstance(arg, str) else arg for arg in args]
    sep, end = str(sep).upper(), str(end).upper()
    builtin_print(*args, sep=sep, end=end)
