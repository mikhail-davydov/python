import json
from collections import ChainMap

with open('zoo.json', encoding='u8') as i_file:
    zoo = ChainMap(*json.load(i_file))

print(sum(zoo[key] for key in zoo))

# course solution
import json
from collections import ChainMap

with open('zoo.json', encoding='utf-8') as js:
    animals = ChainMap(*json.load(js))

print(sum(animals.values()))
