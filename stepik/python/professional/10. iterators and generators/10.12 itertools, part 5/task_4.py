from collections import namedtuple

import itertools

Item = namedtuple('Item', ['name', 'mass', 'price'])

items = [Item('Обручальное кольцо', 7, 49_000),
         Item('Мобильный телефон', 200, 110_000),
         Item('Ноутбук', 2000, 150_000),
         Item('Ручка Паркер', 20, 37_000),
         Item('Статуэтка Оскар', 4000, 28_000),
         Item('Наушники', 150, 11_000),
         Item('Гитара', 1500, 32_000),
         Item('Золотая монета', 8, 140_000),
         Item('Фотоаппарат', 720, 79_000),
         Item('Лимитированные кроссовки', 300, 80_000)]

# Чтение грузоподъемности рюкзака
capacity = int(input())

best_value = 0
best_combination = []

# Перебираем все возможные комбинации предметов
for r in range(1, len(items) + 1):
    for combo in itertools.combinations(items, r):
        total_mass = sum(item.mass for item in combo)
        total_price = sum(item.price for item in combo)

        # Проверяем ограничение по весу и обновляем лучшее решение
        if total_mass <= capacity and total_price > best_value:
            best_value = total_price
            best_combination = list(combo)

# Вывод результата
if best_combination:
    # Сортируем названия предметов в лексикографическом порядке
    names = sorted(item.name for item in best_combination)
    for name in names:
        print(name)
else:
    print("Рюкзак собрать не удастся")

# alt
bag_weight = int(input())
bag_price = -1
bag_items = None

for i in range(1, 11):
    for comb in combinations(items, i):
        comb_price = sum(item.price for item in comb)
        comb_weight = sum(item.mass for item in comb)
        if comb_price > bag_price and comb_weight <= bag_weight:
            bag_items = comb
            bag_price = comb_price

if bag_items:
    for item in sorted(bag_items):
        print(item.name)
else:
    print('Рюкзак собрать не удастся')

# alt
value = int(input())

if min(items, key=lambda x: x.mass).mass > value:
    print('Рюкзак собрать не удастся')
else:
    data = chain.from_iterable(combinations(items, r=i) for i in range(1, 11))
    data_filtered = filter(lambda x: value >= sum(i.mass for i in x), data)
    result = max(data_filtered, key=lambda x: sum(i.price for i in x))
    print(*sorted(i.name for i in result), sep='\n')
