def count_occurrences(word: str, words: str) -> int:
    words_counter = Counter([w.lower() for w in words.split()])
    return words_counter[word.lower()]


word = 'Java'
words = 'Python C++ C# JavaScript Go Assembler'

print(count_occurrences(word, words))

# course solution
from collections import Counter


def count_occurences(word, words):
    words_list = words.lower().split()
    counts = Counter(words_list)
    return counts[word.lower()]
