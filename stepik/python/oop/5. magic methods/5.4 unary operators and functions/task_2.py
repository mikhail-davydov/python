class Money:

    def __init__(self, amount):
        self._amount = amount

    def __str__(self):
        return '{} руб.'.format(self._amount)

    def __pos__(self):
        return self.__class__(abs(self._amount))

    def __neg__(self):
        return self.__class__(-abs(self._amount))


money = Money(100)

print(money)
print(+money)
print(-money)

print(10 * '-')

money = Money(-100)

print(money)
print(+money)
print(-money)
