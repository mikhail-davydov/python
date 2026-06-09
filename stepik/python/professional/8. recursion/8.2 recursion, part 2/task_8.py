def print_digits(number: int):
    if number:
        print(number % 10)
        print_digits(number // 10)


print_digits(12345)


# course
def print_digits(number):
    if number < 10:
        print(number)
    else:
        print(number % 10)
        print_digits(number // 10)
