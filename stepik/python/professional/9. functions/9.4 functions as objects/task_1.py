def numbers_sum(elems: list):
    """Принимает список и возвращает сумму его чисел (int, float),
игнорируя нечисловые объекты. 0 - если в списке чисел нет.
"""
    return sum(filter(lambda x: isinstance(x, (int, float)), elems))


print(numbers_sum([1, '2', 3, 4, 'five']))
print(numbers_sum.__doc__)


# correct for this particular case, using type(x) in filter
def numbers_sum(elems):
    '''Принимает список и возвращает сумму его чисел (int, float),
игнорируя нечисловые объекты. 0 - если в списке чисел нет.'''
    return sum(filter(lambda x: type(x) in (int, float), elems))
