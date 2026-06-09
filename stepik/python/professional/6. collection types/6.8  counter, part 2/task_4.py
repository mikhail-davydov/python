from collections import Counter

words = Counter(map(len, input().lower().split()))
[print(f'Слов длины {key}: {words[key]}') for key in sorted(words, key=words.get)]