def sort_priority(values, group):
    priority_list = sorted(value for value in values if value in group)
    rest_list = sorted(value for value in values if value not in group)

    def join_lists(priority: list, rest: list) -> None:
        nonlocal values
        values.clear()
        values.extend(priority)
        values.extend(rest)

    join_lists(priority_list, rest_list)


numbers = [9, 8, 7, 6, 5, 4, 3, 2, 1]
sort_priority(numbers, (300, 100, 200))

print(numbers)


# base
def sort_priority(numbers, group):
    numbers.sort(key=lambda x: (x not in group, x))
