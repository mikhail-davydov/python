import re


def pluck(data: dict, path: str, default: object = None):
    try:
        path_formatted = re.sub(r'(\w+)', r'["\1"]', path).replace('.', '')
        return eval(f'data{path_formatted}')
    except:
        return default


# alt
def pluck(data, path, default=None):
    value = data
    for key in path.split('.'):
        value = value.get(key, default)

    return value


d = {'a': {'b': 5, 'z': 20}, 'c': {'d': 3}, 'x': 40}
print(pluck(d, 'x'))

print('-' * 10)

d = {'a': {'b': 5, 'z': 20}, 'c': {'d': 3}, 'x': 40}
print(pluck(d, 'a.b'))

print('-' * 10)

d = {'a': {'b': {'c': {'d': {'e': 4}}}}}
print(pluck(d, 'a.b.c'))
