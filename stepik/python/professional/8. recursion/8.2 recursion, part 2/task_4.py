def enumerate_nums(nums):
    def rec(i):
        if i < len(nums) - 1:
            rec(i + 1)
        print(nums[i])

    rec(0)


num = int(input())
numbers = [num]
while num != 0:
    num = int(input())
    numbers.append(num)

enumerate_nums(numbers)


# course solution
def reverse_print():
    n = int(input())
    if n != 0:
        reverse_print()
    print(n)


reverse_print()


# alternative
def recursion_func():
    if num := int(input()):
        recursion_func()
    print(num)


recursion_func()
