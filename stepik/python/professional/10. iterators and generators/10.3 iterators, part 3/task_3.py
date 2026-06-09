def is_iterator(obj):
    try:
        return obj is iter(obj)
    except TypeError:
        return False


beegeek = map(str.upper, 'beegeek')

print(is_iterator(beegeek))


# alt #1
def is_iterator(obj):
    return hasattr(obj, '__next__')


# alt #2
def is_iterator(obj):
    return {'__iter__', '__next__'} < set(dir(obj))
