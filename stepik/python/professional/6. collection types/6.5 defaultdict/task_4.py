from collections import defaultdict


def wins(pairs: list[tuple[str, str]]) -> defaultdict[str, set]:
    students = defaultdict(set)
    for win, lose in pairs:
        students[win].add(lose)
    return students


result = wins([('Тимур', 'Артур'), ('Тимур', 'Дима'), ('Дима', 'Артур')])

for winner, losers in sorted(result.items()):
    print(winner, '->', *sorted(losers))
