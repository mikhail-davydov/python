from collections import namedtuple
from itertools import groupby

Person = namedtuple('Person', ['name', 'age', 'height'])

persons = [Person('Tim', 63, 193), Person('Eva', 47, 158),
           Person('Mark', 71, 172), Person('Alex', 45, 193),
           Person('Jeff', 63, 193), Person('Ryan', 41, 184),
           Person('Ariana', 28, 158), Person('Liam', 69, 193)]


height_sort = lambda person: person.height
persons_grouped = groupby(sorted(persons, key=height_sort), key=height_sort)

for value, group in persons_grouped:
    sorted_group = list(map(lambda person: person.name, sorted(group, key=lambda person: person.name)))
    print(f"{value}: {', '.join(sorted_group)}")


# alt
persons.sort(key=lambda x: (x.height, x.name))
groups = groupby(persons, key=lambda x: x.height)

for key, tpl in groups:
    print(f'{key}: {", ".join(i.name for i in tpl)}')