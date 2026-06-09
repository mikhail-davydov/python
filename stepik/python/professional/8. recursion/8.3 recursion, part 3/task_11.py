def to_binary(number):
    if number < 2:
        return str(number)
    return to_binary(number // 2) + str(number % 2)


print(to_binary(123))

# alt
to_binary = lambda n: str(n) if n < 2 else to_binary(n // 2) + str(n % 2)
