def get_digits(number: int | float) -> list[int]:
    return [int(digit) for digit in str(number) if digit.isdigit()]


annotations = get_digits.__annotations__

print(annotations['return'])


# alt
def get_digits(number: int | float) -> list[int]:
    return list(map(int, str(number).replace('.', '')))
