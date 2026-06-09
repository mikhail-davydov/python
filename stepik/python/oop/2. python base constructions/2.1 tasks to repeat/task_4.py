from collections import Counter

import sys

counter = Counter(map(str.strip, sys.stdin))
print(sum(counter.values()) - len(counter))

# alt
pokemons = [pokemon.strip() for pokemon in sys.stdin]
print(len(pokemons) - len(set(pokemons)))
