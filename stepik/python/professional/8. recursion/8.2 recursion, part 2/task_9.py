def print_digits(number: int):
    if number > 10:
        print_digits(number // 10)
    print(number % 10)


print_digits(12345)


# course
def print_digits(number):
    if number < 10:
        print(number)
    else:
        print_digits(number // 10)
        print(number % 10)
