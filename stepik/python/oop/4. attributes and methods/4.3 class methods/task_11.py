class TextHandler:
    def __init__(self):
        self.words = []

    def add_words(self, text):
        self.words.extend(text.split())

    def get_shortest_words(self):
        if not self.words:
            return self.words
        shortest_len = min(map(len, self.words))
        return [word for word in self.words if len(word) == shortest_len]

    def get_longest_words(self):
        if not self.words:
            return self.words
        longest_len = max(map(len, self.words))
        return [word for word in self.words if len(word) == longest_len]


# alt
class TextHandler:
    def __init__(self):
        self.words = []
        self.shortest = 0
        self.longest = 0

    def add_words(self, words):
        words = words.split()
        self.words.extend(words)
        self.shortest = min(map(len, self.words))
        self.longest = max(map(len, self.words))

    def get_shortest_words(self):
        return [w for w in self.words if len(w) == self.shortest]

    def get_longest_words(self):
        return [w for w in self.words if len(w) == self.longest]


texthandler = TextHandler()

print(texthandler.get_shortest_words())
print(texthandler.get_longest_words())

print('-' * 10)

texthandler = TextHandler()

texthandler.add_words('The world will hold my trial for your sins')
texthandler.add_words('Never meant to see the sky never meant to live')

print(texthandler.get_shortest_words())
print(texthandler.get_longest_words())
