from collections import Counter

words = Counter(input().lower().split())
max_value = max(words.values())
max_words = list(filter(lambda key: words.get(key) == max_value, words))

print(sorted(max_words)[-1])

# course solution
from collections import Counter

words = input().lower().split()
counts = Counter(words)
most_common_word = max(counts, key=lambda w: (counts[w], w))

print(most_common_word)
