from collections import Counter

counts = Counter(input().split(','))
[print(f'{key}: {counts[key]}') for key in sorted(counts)]