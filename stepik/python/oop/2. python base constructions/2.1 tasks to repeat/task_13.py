from typing import Iterator


def annual_return(start, percent, years):
    for _ in range(years):
        start += start * percent / 100
        yield start


# alt
def annual_return(start: int, percent: int, years: int) -> Iterator:
    return (start := start * (1 + percent / 100) for _ in range(years))


for value in annual_return(120000, 10, 3):
    print(round(value))
print('-' * 10)

for value in annual_return(70000, 8, 10):
    print(round(value))
