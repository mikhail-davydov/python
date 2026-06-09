from itertools import combinations

wallet = [100, 100, 50, 50, 50, 50, 20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]
target = 100

# Множество для хранения уникальных комбинаций (как кортежей отсортированных купюр)
unique_ways = set()

# Перебираем все возможные длины комбинаций от 1 до длины кошелька
for r in range(1, len(wallet) + 1):
    # Генерируем все комбинации длины r
    for combo in combinations(wallet, r):
        # Если сумма комбинации равна целевой
        if sum(combo) == target:
            # Сортируем и добавляем в множество (это уберёт дубликаты)
            unique_ways.add(tuple(sorted(combo)))

# Выводим количество уникальных способов
print(len(unique_ways))