def parse_ranges(ranges):
    start_stop = (map(int, rng.split('-')) for rng in ranges.split(','))
    yield from (i for start, stop in start_stop for i in range(start, stop + 1))


print(*parse_ranges('1-2,4-4,8-10'))
print(*parse_ranges('1-10,2-10'))
print(*parse_ranges('7-32'))


# alt
def parse_ranges(ranges):
    parts = (part for part in ranges.split(','))
    pairs = (part.split('-') for part in parts)
    numbers = ((int(a), int(b)) for a, b in pairs)

    for a, b in numbers:
        yield from range(a, b + 1)


# alt
def parse_ranges(ranges: str):
    for r in ranges.split(","):
        start, end = map(int, r.split("-"))
        yield from range(start, end + 1)
