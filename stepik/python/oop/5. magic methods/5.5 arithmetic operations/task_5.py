class Path:

    def __init__(self, *args):
        self._catalogs = []
        for arg in args:
            if isinstance(arg, str):
                self._catalogs.extend(arg.split('/'))
            if isinstance(arg, Path):
                self._catalogs.extend(arg._catalogs)
            if isinstance(arg, list):
                self._catalogs.extend(arg)

    def __str__(self):
        return '/'.join(self._catalogs)

    def __repr__(self):
        return f'{__class__.__name__}({'/'.join(self._catalogs)!r})'

    def __truediv__(self, other):
        if isinstance(other, str):
            return __class__(self._catalogs, other)
        if isinstance(other, Path):
            return __class__(self, other)
        return NotImplemented

    def __itruediv__(self, other):
        if isinstance(other, str):
            self._catalogs.extend(other.split('/'))
            return self
        if isinstance(other, Path):
            self._catalogs.extend(other._catalogs)
            return self
        return NotImplemented


# alt
class Path:
    def __init__(self, *parts):
        parts = (str(part) for part in parts)
        self._path = '/'.join(parts)

    def __str__(self):
        return self._path

    def __repr__(self):
        return f'{self.__class__.__name__}({self._path!r})'

    def __truediv__(self, other):
        if isinstance(other, self.__class__ | str):
            return self.__class__(self._path, other)

        return NotImplemented

    def __itruediv__(self, other):
        if isinstance(other, self.__class__ | str):
            self._path += '/' + str(other)
            return self

        return NotImplemented


path = Path('home', 'user', 'docs')

print(str(path))
print(repr(path))

print(10 * '-')

path = Path(Path('home'), 'user', Path('docs'))
print(path)

print(10 * '-')

path = Path('home', 'user') / Path('docs')
print(path)

print(10 * '-')

path1 = Path('home')
path2 = Path('user/docs')
path3 = path1 / path2
print(path1)
print(path2)
print(path3)

print(10 * '-')

# TEST_5:
path = Path('home')
path /= 'user'
print(path)

print(10 * '-')

# TEST_11:
path1 = Path('home', 'user')
path2 = Path('projects', 'python')
path3 = Path('docs', '2025')
path4 = Path('book.pdf')

path_a = path1 / path2
print(path_a)

path_b = path_a / path3
print(path_b)

path_c = path_b / path4
print(path_c)

path_d = Path('var', 'log') / 'system'
print(path_d)

path_d /= Path('kernel')
print(path_d)

combined = Path('tmp', 'files') / '2025' / Path('reports/omg') / 'report.pdf'
print(combined)

seq_path = Path('home', 'user')
seq_path /= Path('downloads', 'photos')
print(seq_path)

seq_path /= 'vacation'
print(seq_path)

seq_path /= Path('2025', 'summer', 'trip.jpg')
print(seq_path)
