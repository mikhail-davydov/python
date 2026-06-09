def number_of_frogs(year: int) -> int:
    if year == 1:
        return 77
    return 3 * (number_of_frogs(year - 1) - 30)


print(number_of_frogs(10))

# alternative
number_of_frogs = lambda year: 77 if year == 1 else 3 * (number_of_frogs(year - 1) - 30)
