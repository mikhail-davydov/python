def stop_on(iterable, obj):
    for item in iterable:
        if item != obj:
            yield item
        else:
            return

# alt
def stop_on(iterable, obj):
    it = iter(iterable)
    return iter(lambda: next(it), obj)


numbers = [1, 2, 3, 4, 5]

print(*stop_on(numbers, 4))
