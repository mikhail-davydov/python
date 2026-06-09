def custom_isinstance(objects, typeinfo):
    return sum(1 for obj in objects if isinstance(obj, typeinfo))


numbers = [1, 'two', 3.0, 'четыре', 5, 6.0]
print(custom_isinstance(numbers, list))


# alt
def custom_isinstance(objects, typeinfo):
    return sum(isinstance(i, typeinfo) for i in objects)
