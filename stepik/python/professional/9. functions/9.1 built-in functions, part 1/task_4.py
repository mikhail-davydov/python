def non_negative_even(numbers):
    return all(num == abs(num) and num % 2 == 0 for num in numbers)


print(non_negative_even([0, 0, 0, 0, 0]))