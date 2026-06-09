# 1
import pickle
from collections import namedtuple


Animal = namedtuple('Animal', ['name', 'family', 'sex', 'color'])

with open('data.pkl', 'rb') as f:
    animals = pickle.load(f)

for animal in animals:
    for field, value in animal._asdict().items():
        print(f"{field}: {value}")
    print()


# 2
from collections import namedtuple
import pickle

Animal = namedtuple('Animal', ('name', 'family', 'sex', 'color'))

with open('data.pkl', 'rb') as fi:
    animals = pickle.load(fi)

for animal in animals:
    for key, value in zip(Animal._fields, animal):
        print(f'{key}: {value}')
    print()