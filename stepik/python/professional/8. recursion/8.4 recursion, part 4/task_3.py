def get_value(nested_dicts, key):
    if key in nested_dicts:
        return nested_dicts[key]
    for value in nested_dicts.values():
        if isinstance(value, dict):
            result = get_value(value, key)
            if result:
                return result

data = {'first_name': 'Alyson', 'last_name': 'Hannigan', 'birthday': {'day': 24, 'month': 'March', 'year': 1974}}

print(get_value(data, 'birthday'))
