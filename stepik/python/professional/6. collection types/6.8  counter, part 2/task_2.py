from collections import Counter

words = Counter(input().lower().split())
min_value = min(words.values())
min_words = list(filter(lambda key: words.get(key) == min_value, words))

print(*sorted(min_words), sep=', ')