from collections import Counter


def scrabble(symbols, word):
    symbols_counts = Counter(symbols.lower())
    word_counts = Counter(word.lower())
    return word_counts <= symbols_counts


print(scrabble('bbbbbeeeeegggggggeeeeeekkkkk', 'Beegeek'))
print(scrabble('begk', 'beegeek'))
print(scrabble('beegeek', 'beegeek'))
