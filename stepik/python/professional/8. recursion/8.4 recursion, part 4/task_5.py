def dict_travel(nested_dicts: dict):
    def get_all_values(nested_dicts: dict, path: list):
        for key, value in nested_dicts.items():
            if path:
                path.pop()
            path.append(key)
            if not isinstance(value, dict):
                dict_key = '.'.join(path)
                key_value_dict[dict_key] = value
            elif isinstance(value, dict):
                new_path = path.copy()
                new_path.append(key)
                get_all_values(value, new_path)

    key_value_dict = {}
    path = []
    get_all_values(nested_dicts, path)
    for key in sorted(key_value_dict):
        print(key, key_value_dict[key], sep=': ')


data = {'a': 1, 'b': {'c': 30, 'a': 10, 'b': 20}}

dict_travel(data)


# base
def dict_travel(nested_dicts):
    def traverse(d, prefix=''):
        for key, value in sorted(d.items()):
            path = f'{prefix}.{key}' if prefix else key
            if isinstance(value, dict):
                traverse(value, path)
            else:
                print(f'{path}: {value}')

    traverse(nested_dicts)
