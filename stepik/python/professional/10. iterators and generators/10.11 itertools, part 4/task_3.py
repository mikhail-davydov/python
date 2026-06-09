from itertools import groupby

words = input().split()
words_sorted = sorted(words, key=lambda x: (len(x), x))
words_grouped = groupby(words_sorted, key=lambda x: len(x))
for key, group in words_grouped:
    print(f'{key} -> {', '.join(group)}')

# alt
words = input().split()
words.sort(key=lambda w: (len(w), w))
for length, group in groupby(words, key=len):
    print(f'{length} -> {', '.join(group)}')
