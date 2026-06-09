from collections import ChainMap


def get_all_values(chainmap: ChainMap, key: object) -> set:
    return {mapping[key] for mapping in chainmap.maps if key in mapping}


chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})
result = get_all_values(chainmap, 'age')

print(result)