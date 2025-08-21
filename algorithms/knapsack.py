import json
from typing import List


class Item:

    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price


class Knapsack:

    def __init__(self, capacity, items):
        self.capacity = capacity
        self.items = items


def pack(knapsack: Knapsack, items: List[Item]) -> Knapsack:
    n_items = len(items)
    m_capacity = knapsack.capacity

    # инициализируем матрицу решений
    dp_matrix = [[(0, [])] * (m_capacity + 1) for _ in range(n_items + 1)]

    for item in range(1, n_items + 1):
        for weight in range(1, m_capacity + 1):
            if items[item - 1].weight <= weight:
                # Выбираем максимум между включением и исключением предмета
                previous_max_price = dp_matrix[item - 1][weight][0]
                previous_items_list = dp_matrix[item - 1][weight][1]
                current_max_price = items[item - 1].price + dp_matrix[item - 1][weight - items[item - 1].weight][0]
                if previous_max_price >= current_max_price:
                    dp_matrix[item][weight] = (previous_max_price, previous_items_list.copy())
                else:
                    current_items_list = dp_matrix[item - 1][weight - items[item - 1].weight][1].copy()
                    current_items_list.append(items[item - 1])
                    dp_matrix[item][weight] = (current_max_price, current_items_list)
            else:
                # Не можем включить предмет
                dp_matrix[item][weight] = dp_matrix[item - 1][weight]

    knapsack.items = dp_matrix[n_items][m_capacity][1]
    return knapsack


items = [
    Item("water", 3, 10),
    Item("book", 1, 3),
    Item("food", 2, 9),
    Item("jacket", 2, 5),
    Item("camera", 1, 6),
    ]

knapsack = Knapsack(6, [])

print("items in the knapsack:", json.dumps(pack(knapsack, items).items, indent=2, default=vars))
