def get_first_last(str_obj):
    if not str_obj:
        return 0
    if len(str_obj) == 1:
        return ord(str_obj[0])
    return ord(str_obj[0]) * ord(str_obj[-1]) + get_first_last(str_obj[1:-1])


def get_nult(str_obj):
    return sum(ord(value) * i * (-1, 1)[i % 2] for i, value in enumerate(str_obj, 1))


def hash_function(obj):
    str_obj = str(obj)
    temp1 = get_first_last(str_obj)
    temp2 = get_nult(str_obj)
    return (temp1 * temp2) % 123456791


# alt
def hash_function(obj):
    obj = str(obj)
    middle = len(obj) // 2
    temp1, temp2 = ord(obj[middle]) * (len(obj) % 2 == 1), 0

    for i in range(middle):
        temp1 += ord(obj[i]) * ord(obj[-1 - i])

    for i, c in enumerate(obj, 1):
        temp2 += ord(c) * i * ((-1) ** (i + 1))

    return temp1 * temp2 % 123456791
