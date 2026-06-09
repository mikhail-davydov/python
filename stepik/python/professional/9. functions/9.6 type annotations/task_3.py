from collections import deque


def cyclic_shift(numbers: list[int | float], step: int) -> None:
    d = deque(numbers)
    d.rotate(step)
    numbers.clear()
    numbers.extend(d)


numbers = [1, 2, 3, 4, 5]
cyclic_shift(numbers, -2)

print(numbers)


# alt
def cyclic_shift(numbers: list[int | float], step: int) -> None:
    n = len(numbers)
    step %= n
    temp = numbers.copy()
    for i in range(n):
        numbers[(i + step) % n] = temp[i]
