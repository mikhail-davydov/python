class ReversibleString:

    def __init__(self, string):
        self._string = string

    def __neg__(self):
        return ReversibleString(self._string[::-1])

    def __str__(self):
        return self._string


string = ReversibleString('python')

print(string)
print(-string)
