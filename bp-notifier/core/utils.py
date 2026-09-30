from core.types import Number


def to_number(shelves: str) -> Number:
    try:
        return int(shelves)
    except ValueError:
        return float(shelves)
