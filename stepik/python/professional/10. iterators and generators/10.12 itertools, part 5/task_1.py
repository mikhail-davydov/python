from itertools import permutations

s = input().strip()
unique_permutations = sorted(set(permutations(s)))
for perm in unique_permutations:
    print(''.join(perm))
