from collections import OrderedDict


def custom_sort(ordered_dict: OrderedDict, by_values: bool = False) -> None:
    sort_func = lambda item: item[by_values]
    for key, _ in sorted(ordered_dict.items(), key=sort_func):
        ordered_dict.move_to_end(key)


data = OrderedDict(Earth=3, Mercury=1, Mars=4, Venus=2)
custom_sort(data, by_values=True)

print(*data.items())


# course solution
def custom_sort(data, by_values=False):
    if by_values:
        for key in sorted(data, key=lambda k: data[k]):
            data.move_to_end(key)
    else:
        for key in sorted(data):
            data.move_to_end(key)


# alternative solution
def custom_sort(ordered_dict: OrderedDict, by_values: bool = False) -> None:
    order = sorted(ordered_dict, key=ordered_dict.get if by_values else None)
    for key in order:
        ordered_dict.move_to_end(key)


# alternative solution #2
def custom_sort(data, by_values=False):
    for key in sorted(data, key=(None, data.get)[by_values]):
        data.move_to_end(key)
