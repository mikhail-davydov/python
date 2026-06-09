class MutableString:
    def __init__(self, string: str = ''):
        self._string = string

    def lower(self):
        self._string = self._string.lower()

    def upper(self):
        self._string = self._string.upper()

    def __repr__(self):
        return f'{self.__class__.__name__}({self._string!r})'

    def __str__(self):
        return self._string

    def __len__(self):
        return len(self._string)

    def __iter__(self):
        return iter(self._string)

    def __add__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self.__class__(self._string + other._string)

    def __getitem__(self, key):
        return self.__class__(self._string[key])

    def __setitem__(self, key, value):
        string_lst = list(self._string)
        string_lst[key] = value
        self._string = ''.join(string_lst)

    # alt
    # def __setitem__(self, key, value):
    #     self.string = self.string.replace(self.string[key], value)

    def __delitem__(self, key):
        string_lst = list(self._string)
        del string_lst[key]
        self._string = ''.join(string_lst)

    # alt
    # def __delitem__(self, key):
    #     self.string = self.string.replace(self.string[key], '')

    __radd__ = __add__
