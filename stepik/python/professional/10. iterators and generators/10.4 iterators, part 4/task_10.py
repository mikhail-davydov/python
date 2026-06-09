class Alphabet:
    def __init__(self, lang):
        self.start = ('a', 'а')[lang == 'ru']
        self.current = self.start

    def __next__(self):
        value = self.current
        self.current = self.start if self.current in ('z', 'я') else chr(ord(self.current) + 1)
        return value


    def __iter__(self):
        return self


en_alpha = Alphabet('en')

letters = [next(en_alpha) for _ in range(28)]

print(*letters)