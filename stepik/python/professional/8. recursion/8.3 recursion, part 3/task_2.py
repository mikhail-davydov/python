num_sum = lambda x: x if x < 10 else x % 10 + num_sum(x // 10)

print(num_sum(int(input())))


# alternative
def sum_digit(num):
    return num if not num else num % 10 + sum_digit(num // 10)


print(sum_digit(int(input())))
