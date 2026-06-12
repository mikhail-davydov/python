import operator

import string


class CaesarCipher:
    def __init__(self, shift: int):
        self.shift = shift

    def encode(self, s: str):
        chars = []
        for c in s:
            if c in string.ascii_lowercase:
                shifted_c = self._get_char(c, string.ascii_lowercase, operator.add)
                chars.append(shifted_c)
            elif c in string.ascii_uppercase:
                shifted_c = self._get_char(c, string.ascii_uppercase, operator.add)
                chars.append(shifted_c)
            else:
                chars.append(c)
        return ''.join(chars)

    def decode(self, s: str):
        chars = []
        for c in s:
            if c in string.ascii_lowercase:
                shifted_c = self._get_char(c, string.ascii_lowercase, operator.sub)
                chars.append(shifted_c)
            elif c in string.ascii_uppercase:
                shifted_c = self._get_char(c, string.ascii_uppercase, operator.sub)
                chars.append(shifted_c)
            else:
                chars.append(c)
        return ''.join(chars)

    def _get_char(self, c, s, func):
        idx = s.index(c)
        idx_shifted = func(idx, self.shift) % len(s)
        return s[idx_shifted]


# alt

from string import ascii_lowercase as low, ascii_uppercase as up


class CaesarCipher:
    def __init__(self, key):
        self._encode = str.maketrans(low, low[key:] + low[:key]) | str.maketrans(up, up[key:] + up[:key])
        self._decode = {v: k for k, v in self._encode.items()}

    def encode(self, string):
        return str.translate(string, self._encode)

    def decode(self, string):
        return str.translate(string, self._decode)
