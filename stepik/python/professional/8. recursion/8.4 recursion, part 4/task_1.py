def recursive_sum(nested_lists):
    total = 0
    if isinstance(nested_lists, int):
        total += nested_lists
    if isinstance(nested_lists, list):
        for elem in nested_lists:
            total += recursive_sum(elem)
    return total


my_list = []

print(recursive_sum(my_list))


# alt
def recursive_sum(nested_lists):
    s = 0
    for i in nested_lists:
        s += i if type(i) is int else recursive_sum(i)
    return s
