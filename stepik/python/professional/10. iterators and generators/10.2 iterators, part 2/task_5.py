def get_min_max(iterable):
    try:
        iterator = iter(iterable)
        elem = next(iterator)
        min_elem = max_elem = elem
        while True:
            try:
                elem = next(iterator)
                if elem < min_elem:
                    min_elem = elem
                if elem > max_elem:
                    max_elem = elem
            except:
                return min_elem, max_elem
    except:
        return None


iterable = iter(range(10))

print(get_min_max(iterable))


# alt
def get_min_max(iterable):
    iterable = iter(iterable)
    try:
        smallest = largest = next(iterable)
    except:
        return None
    for elem in iterable:
        if elem < smallest:
            smallest = elem
        if elem > largest:
            largest = elem
    return smallest, largest
