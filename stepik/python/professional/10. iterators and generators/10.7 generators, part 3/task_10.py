def with_previous(iterable):
    previous = None
    for item in iterable:
        yield item, previous
        previous = item


iterator = iter('stepik')

print(*with_previous(iterator))
