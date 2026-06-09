from functools import total_ordering


@total_ordering
class Version:

    def __init__(self, version):
        version_nums = version.split('.')
        self._version = tuple(
            int(version_nums[i]) if i < len(version_nums) else 0
            for i in range(3)
        )

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._version == other._version
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return self._version < other._version
        return NotImplemented

    def __str__(self):
        return '.'.join(map(str, self._version))

    def __repr__(self):
        class_name = self.__class__.__name__
        version_str = '.'.join(map(str, self._version))
        return f'{class_name}({version_str!r})'


# alt
@total_ordering
class Version:
    def __init__(self, version):
        self._parts = [int(i) for i in version.split('.')]
        self._parts += [0] * (3 - len(self._parts))

    def __str__(self):
        return '{}.{}.{}'.format(*self._parts)

    def __repr__(self):
        return "Version('{}.{}.{}')".format(*self._parts)

    def __eq__(self, other):
        if isinstance(other, Version):
            return self._parts == other._parts
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Version):
            return self._parts < other._parts
        return NotImplemented


print(Version('3.0.3') == Version('1.11.28'))
print(Version('3.0.3') < Version('1.11.28'))
print(Version('3.0.3') > Version('1.11.28'))
print(Version('3.0.3') <= Version('1.11.28'))
print(Version('3.0.3') >= Version('1.11.28'))

print(10 * '-')

print(Version('3') == Version('3.0'))
print(Version('3') == Version('3.0.0'))
print(Version('3.0') == Version('3.0.0'))

print(10 * '-')

versions = [Version('2'), Version('2.1'), Version('1.9.1')]

print(sorted(versions))
print(min(versions))
print(max(versions))
