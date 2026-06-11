from dataclasses import dataclass, field


@dataclass(frozen=True)
class MusicAlbum:
    title: str
    artist: str
    genre: str = field(repr=False, compare=False)
    year: int = field(repr=False)


# alt

from dataclasses import field, make_dataclass

MusicAlbum = make_dataclass(
    'MusicAlbum',
    [
        ('title', str),
        ('artist', str),
        ('genre', str, field(repr=False, compare=False)),
        ('year', int, field(repr=False))
    ],
    frozen=True
)
