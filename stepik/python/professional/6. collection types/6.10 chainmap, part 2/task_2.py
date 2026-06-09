from collections import ChainMap


def deep_update(chainmap: ChainMap, key, value: object) -> None:
    if key not in chainmap:
        chainmap.update({key: value})
        return
    [mapping.update({key: value}) for mapping in chainmap.maps if key in mapping]


chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})
deep_update(chainmap, 'age', 20)

print(chainmap)


# course solution

def deep_update(chainmap, key, value):
    for d in chainmap.maps:
        if key in d:
            d[key] = value
    chainmap.setdefault(key, value)
