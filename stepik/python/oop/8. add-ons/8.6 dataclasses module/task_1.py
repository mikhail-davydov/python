from dataclasses import dataclass


@dataclass
class City:
    name: str
    population: int
    founded: str


# alt

from dataclasses import make_dataclass

City = make_dataclass('City', ('name', 'population', 'founded'))
