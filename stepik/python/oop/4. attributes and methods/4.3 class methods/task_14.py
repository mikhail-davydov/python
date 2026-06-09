class Wordplay:
    def __init__(self, words: list = None):
        self.words = []
        if words:
            self.words.extend(words)

    def add_word(self, word):
        if word not in self.words:
            self.words.append(word)

    def words_with_length(self, n):
        return [word for word in self.words if len(word) == n]

    def only(self, *args):
        if not args:
            return []
        return [word for word in self.words if set(word).issubset(set(args))]

    def avoid(self, *args):
        if not args:
            return self.words
        return [word for word in self.words if set(word).isdisjoint(set(args))]


wordplay = Wordplay()

print(wordplay.words_with_length(1))
print(wordplay.only('a', 'b', 'c'))
print(wordplay.avoid('a', 'b', 'c'))

print('-' * 10)

wordplay = Wordplay()

print(wordplay.words)
wordplay.add_word('bee')
wordplay.add_word('geek')
print(wordplay.words)

print('-' * 10)

wordplay = Wordplay(['bee', 'geek', 'cool', 'stepik'])

wordplay.add_word('python')
print(wordplay.words_with_length(4))

print('-' * 10)

wordplay = Wordplay(['o', 'to', 'otto', 'top', 't'])

print(wordplay.only('o', 't'))
