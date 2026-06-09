from itertools import groupby


def group_anagrams(words):
    sort_key = lambda w: sorted(w)
    return sorted(tuple(groups) for _, groups in groupby(sorted(words, key=sort_key), key=sort_key))


# alt
def group_anagrams(words):
    sorted_words = sorted(words, key=sorted)
    groups = groupby(sorted_words, key=sorted)
    return [tuple(group) for _, group in groups]


groups = group_anagrams(['evil', 'father', 'live', 'levi', 'book', 'afther', 'boko'])
print(*groups)

groups = group_anagrams(['evil', 'father', 'book', 'stepik', 'beegeek'])
print(*groups)

groups = group_anagrams(['крона', 'сеточка', 'тесачок', 'лучик', 'стоечка', 'норка', 'чулки'])
print(*groups)

groups = group_anagrams(['катет', 'кета'])
print(*groups)
