def get_min_max(data):
    if data:
        return min(enumerate(data), key=lambda x: x[1])[0], max(enumerate(data), key=lambda x: x[1])[0]


data = [2, 3, 8, 1, 7]

print(get_min_max(data))


# alt #1
def get_min_max(data):
    if not data:
        return None

    min_idx = max_idx = 0
    for idx, elem in enumerate(data):
        if elem < data[min_idx]:
            min_idx = idx
        if elem > data[max_idx]:
            max_idx = idx

    return min_idx, max_idx


# alt #2
def get_min_max(data):
    if data:
        return data.index(min(data)), data.index(max(data))


# alt #3
def get_min_max(data):
    if not data:
        return None
    d = dict(enumerate(data))
    return min(d, key=d.get), max(d, key=d.get)
