from collections import ChainMap, Counter

bread = {'булочка с кунжутом': 15, 'обычная булочка': 10, 'ржаная булочка': 15}
meat = {'куриный бифштекс': 50, 'говяжий бифштекс': 70, 'рыбный бифштекс': 40}
sauce = {'сливочно-чесночный': 15, 'кетчуп': 10, 'горчица': 10, 'барбекю': 15, 'чили': 15}
vegetables = {'лук': 10, 'салат': 15, 'помидор': 15, 'огурцы': 10}
toppings = {'сыр': 25, 'яйцо': 15, 'бекон': 30}

ingredients = ChainMap(bread, meat, sauce, vegetables, toppings)

order = Counter(input().split(','))

total = f'ИТОГ: {sum(ingredients[key] * amount for key, amount in order.items())}р'

max_ingredient_len = max(map(len, order))
max_ingredient_len_with_amount = 0
for ingredient in sorted(order):
    ingredient_with_amount = f'{ingredient:{max_ingredient_len}} x {order[ingredient]}'
    print(ingredient_with_amount)
    max_ingredient_len_with_amount = max(len(ingredient_with_amount), max_ingredient_len_with_amount)

dashes = max(max_ingredient_len_with_amount, len(total)) * '-'
print(dashes)
print(total)

# course solution
from collections import ChainMap, Counter

bread = {'булочка с кунжутом': 15, 'обычная булочка': 10, 'ржаная булочка': 15}
meat = {'куриный бифштекс': 50, 'говяжий бифштекс': 70, 'рыбный бифштекс': 40}
sauce = {'сливочно-чесночный': 15, 'кетчуп': 10, 'горчица': 10, 'барбекю': 15, 'чили': 15}
vegetables = {'лук': 10, 'салат': 15, 'помидор': 15, 'огурцы': 10}
toppings = {'сыр': 25, 'яйцо': 15, 'бекон': 30}

ingredients = ChainMap(bread, meat, sauce, vegetables, toppings)

order = Counter(input().split(','))

total = f'ИТОГ: {sum(ingredients[key] * amount for key, amount in order.items())}р'

max_ingredient_len = max(map(len, order))
max_ingredient_len_with_amount = 0
for ingredient in sorted(order):
    ingredient_with_amount = f'{ingredient:{max_ingredient_len}} x {order[ingredient]}'
    print(ingredient_with_amount)
    max_ingredient_len_with_amount = max(len(ingredient_with_amount), max_ingredient_len_with_amount)

dashes = max(max_ingredient_len_with_amount, len(total)) * '-'
print(dashes)
print(total)
