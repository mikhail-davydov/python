def get_all_values(nested_dicts, key):
    hobbies = set()
    if key in nested_dicts:
        hobbies.add(nested_dicts[key])
    for value in nested_dicts.values():
        if isinstance(value, dict):
            hobbies.update(get_all_values(value, key))
    return hobbies


my_dict = {'Arthur': {'hobby': 'videogames', 'drink': 'cacao'}, 'Timur': {'hobby': 'math'}}
result = get_all_values(my_dict, 'top_grade')

print(len(sorted(result)))


# base
def get_all_values(data, key):
    values = set()
    if key in data:
        values.add(data[key])
    for item in data.values():
        if isinstance(item, dict):
            values |= get_all_values(item, key)
    return values
