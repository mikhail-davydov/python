from collections import ChainMap


def get_value(chainmap: ChainMap, key: object, from_left: bool = True) -> None | object:
    search_chainmap = chainmap if from_left else ChainMap(*reversed(chainmap.maps))
    return search_chainmap.get(key, None)


chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})

print(get_value(chainmap, 'age'))

# alternative solution
from collections import ChainMap


def get_value(chainmap, key, from_left=True):
    if not from_left:
        chainmap.maps.reverse()
    return chainmap.get(key, None)
