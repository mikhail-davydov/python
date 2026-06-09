def range_sum(numbers, start, end) -> int:
    return numbers[start] if start == end else numbers[start] + range_sum(numbers, start + 1, end)


print(range_sum([1, 2, 3, 4, 5, 6, 7, 8, 9], 0, 0))
