import itertools

wallet = [100, 50, 20, 10, 5]
target = 100

# Множество для хранения уникальных комбинаций (как кортежей отсортированных купюр)
unique_ways = set()

# Перебираем все возможные длины комбинаций от 1 до 20 (20 — с запасом, так как минимальная купюра 5)
for r in range(1, 21):
    # Генерируем все комбинации с повторениями длины r
    for combo in itertools.combinations_with_replacement(wallet, r):
        if sum(combo) == target:
            # Добавляем отсортированную комбинацию в множество (для уникальности)
            unique_ways.add(combo)  # combinations_with_replacement уже возвращает отсортированные кортежи

# Выводим количество уникальных способов
print(len(unique_ways))