def unique(iterable):
    past = set()
    for item in iterable:
        if item not in past:
            yield item
            past.add(item)


iterator = iter('111222333')
uniques = unique(iterator)

print(next(uniques))
print(next(uniques))
print(next(uniques))


# alt
def unique(numbers):
    yield from (dict.fromkeys(numbers))
