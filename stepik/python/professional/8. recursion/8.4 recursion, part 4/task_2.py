def linear(nested_lists):
    flatten = []
    for elem in nested_lists:
        if isinstance(elem, int):
            flatten.append(elem)
        elif isinstance(elem, list):
            flatten.extend(linear(elem))
    return flatten


my_list = [10, 20, 30, 40, 50]

print(linear(my_list))


# alt
def linear(nested_lists: list) -> list:
    if not nested_lists:
        return []
    if isinstance(nested_lists[0], list):
        return linear(nested_lists[0]) + linear(nested_lists[1:])
    return [nested_lists[0]] + linear(nested_lists[1:])
