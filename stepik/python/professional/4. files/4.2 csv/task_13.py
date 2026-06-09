import csv
import sys

cheapest_product = None
cheapest_price = float('inf')
cheapest_store = None

with open('prices.csv', encoding='utf-8') as file:
    reader = csv.reader(file, delimiter=';')
    headers = next(reader)  # Пропускаем заголовки
    
    for row in reader:
        store = row[0]
        for i, price_str in enumerate(row[1:], start=1):
            product = headers[i]
            price = int(price_str)
            
            # Проверяем, является ли текущий продукт дешевле
            # или дешевле и лексикографически меньше
            if (price < cheapest_price or 
                (price == cheapest_price and product < cheapest_product) or
                (price == cheapest_price and product == cheapest_product and store < cheapest_store)):
                cheapest_product = product
                cheapest_price = price
                cheapest_store = store

# Явное указание кодировки вывода для Windows
sys.stdout.reconfigure(encoding='utf-8')
print(f'{cheapest_product}: {cheapest_store}')