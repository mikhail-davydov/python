import functools
import json


def jsonify(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return json.dumps(func(*args, **kwargs))

    return wrapper


@jsonify
def make_user(id, live, options):
    return {'id': id, 'live': live, 'options': options}


print(make_user(4, False, None))


@jsonify
def make_list(n):
    return list(range(1, n + 1))


print(make_list(10))


@jsonify
def make_str(s1, s2):
    return (s1 + s2) * 5


print(make_str('bee', 'geek'))
