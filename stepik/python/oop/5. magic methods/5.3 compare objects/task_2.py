from functools import total_ordering


@total_ordering
class Word:

    def __init__(self, word: str):
        self._word = word

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return len(self._word) == len(other._word)
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return len(self._word) < len(other._word)
        return NotImplemented

    def __str__(self):
        return self._word.capitalize()

    def __repr__(self):
        class_name = type(self).__name__
        return f'{class_name}({self._word!r})'


print(Word('bee') == Word('hey'))
print(Word('bee') < Word('geek'))
print(Word('bee') > Word('geek'))
print(Word('bee') <= Word('geek'))
print(Word('bee') >= Word('gee'))

print(10 * '-')

words = [Word('python'), Word('bee'), Word('geek')]

print(sorted(words))
print(min(words))
print(max(words))
