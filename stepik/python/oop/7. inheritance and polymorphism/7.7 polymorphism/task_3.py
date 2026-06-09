from abc import ABC, abstractmethod


class Paragraph(ABC):
    def __init__(self, length: int):
        self.length = length
        self._words = []
        self._lines = []

    @property
    @abstractmethod
    def left(self):
        return NotImplemented

    def add(self, words: str):
        self._lines.clear()
        self._words.extend(words.split())
        start = self._words[0]
        for word in self._words[1:]:
            phrase = start + ' ' + word
            if len(phrase) <= self.length:
                start = phrase
            else:
                self._lines.append(start)
                start = word
        self._lines.append(start)

    def end(self):
        for line in self._lines:
            if self.left:
                print(f'{line}')
            else:
                align = '>'
                print(f'{line:{align}{self.length}}')
        self._lines.clear()
        self._words.clear()


class LeftParagraph(Paragraph):
    @property
    def left(self):
        return True


class RightParagraph(Paragraph):
    @property
    def left(self):
        return False
