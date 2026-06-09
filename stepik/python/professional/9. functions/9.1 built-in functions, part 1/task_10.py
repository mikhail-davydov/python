def zip_longest(*args, fill=None):
    max_len = len(max(args, key=len))
    for lst in args:
        while len(lst) < max_len:
            lst.append(fill)
    return list(zip(*args))


data = [[1, 2, 3, 4, 5], ['one', 'two', 'three'], ['I', 'II']]
print(zip_longest(*data))


# alt
def zip_longest(*args, fill=None):
    max_len = max(map(len, args))
    [l.extend([fill] * (max_len - len(l))) for l in args]
    return list(zip(*args))
