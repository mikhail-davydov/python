def hash_as_key(objects: list) -> dict:
    hash_dict = {}
    for obj in objects:
        obj_hash = hash(obj)
        if obj_hash in hash_dict:
            value = hash_dict[obj_hash]
            if isinstance(value, list):
                value.append(obj)
            else:
                hash_dict[obj_hash] = [value, obj]
        else:
            hash_dict[obj_hash] = obj
    return hash_dict


data = [11, 22, 33, 44, 55, 66, 77, 88, 99, 111]

print(hash_as_key(data))

# base
from collections import defaultdict


def hash_as_key(objects):
    result = defaultdict(list)
    for obj in objects:
        result[hash(obj)].append(obj)
    return {k: v[0] if len(v) == 1 else v for k, v in result.items()}
