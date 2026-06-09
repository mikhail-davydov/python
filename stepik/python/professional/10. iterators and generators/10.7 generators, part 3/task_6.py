def nonempty_lines(file):
    with open(file, encoding='u8') as i_file:
        yield from (
            line.strip() if len(line.strip()) <= 25 else '...'
            for line in i_file
            if line.strip()
        )


lines = nonempty_lines('data.csv')

print(next(lines))
print(next(lines))
print(next(lines))
print(next(lines))


# alt
def nonempty_lines(file):
    with open(file, encoding='utf-8') as f:
        for line in f:
            stripped = line.strip()
            if stripped:
                yield '...' if len(stripped) > 25 else stripped
