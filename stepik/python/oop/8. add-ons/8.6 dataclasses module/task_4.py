from dataclasses import dataclass, field, make_dataclass


@dataclass(order=True)
class FootballPlayer:
    name: str = field(compare=False)
    surname: str = field(compare=False)
    value: int = field(repr=False)


@dataclass
class FootballTeam:
    name: str
    players: list = field(default_factory=list, repr=False, compare=False)

    def add_players(self, *players):
        self.players.extend(players)


# alt

FootballPlayer = make_dataclass(
    'FootballPlayer',
    [
        ('name', str, field(compare=False)),
        ('surname', str, field(compare=False)),
        ('value', int, field(repr=False))
    ],
    order=True
)

FootballTeam = make_dataclass(
    'FootballTeam',
    [
        ('name', str),
        ('players', list, field(default_factory=list, compare=False, repr=False))
    ],
    namespace={
        'add_players': lambda self, *players: self.players.extend(players)
    }
)
