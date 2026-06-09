def my_pow(number):
    return sum(int(c) ** ind for ind, c in enumerate(str(number), 1))


print(my_pow(139))