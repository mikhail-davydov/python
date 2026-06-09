from itertools import combinations


def inversions(sequence):
    s_len = len(sequence)
    return sum(
        1 if i < j and sequence[i] > sequence[j] else 0
        for i in range(s_len - 1)
        for j in range(1, s_len)
    )


# alt
def inversions(sequence: list[int]) -> int:
    result = 0
    for seq in combinations(sequence, 2):
        current_item, next_item = seq
        if current_item > next_item:
            result += 1
    return result


sequence = [3, 1, 4, 2]
print(inversions(sequence))

sequence = [1, 2, 3, 4, 5]
print(inversions(sequence))

sequence = [4, 3, 2, 1]
print(inversions(sequence))

sequence = [1, 1, 1, 1, 1, 1]
print(inversions(sequence))
