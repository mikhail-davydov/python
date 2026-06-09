from functools import singledispatchmethod


class IPAddress:
    @singledispatchmethod
    def __init__(self, ipaddress):
        self._ipaddress = ipaddress

    @__init__.register(tuple)
    @__init__.register(list)
    def _(self, ipaddress):
        self._ipaddress = '.'.join(map(str, ipaddress))

    def __str__(self):
        return self._ipaddress

    def __repr__(self):
        class_name = type(self).__name__
        return f"{class_name}('{self._ipaddress}')"


# alt
class IPAddress:
    def __init__(self, ipaddress):
        if isinstance(ipaddress, str):
            self.ipaddress = ipaddress
        elif isinstance(ipaddress, (list, tuple)):
            self.ipaddress = '.'.join(map(str, ipaddress))

    def __str__(self):
        return self.ipaddress

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.ipaddress}')"


ip = IPAddress('8.8.1.1')

print(str(ip))
print(repr(ip))

print(10 * '-')

ip = IPAddress([1, 1, 10, 10])

print(str(ip))
print(repr(ip))

print(10 * '-')

ip = IPAddress((1, 1, 11, 11))

print(str(ip))
print(repr(ip))
