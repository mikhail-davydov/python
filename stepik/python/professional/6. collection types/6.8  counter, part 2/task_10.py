import csv
import json
from collections import Counter

counter = Counter()
for i in range(1, 5):
    with open(f'quarter{i}.csv', encoding='u8') as i_file:
        reader = csv.reader(i_file)
        next(reader)
        for line in reader:
            name, *volumes = line
            counter[name] += sum(map(int, volumes))

# print(counter)

with open('prices.json', encoding='u8') as i_file:
    prices = json.load(i_file)

# print(prices)

print(sum([prices[key] * volume for key, volume in counter.items()]))

# course solution
import csv
import json
from collections import Counter

QUARTERS = ['quarter1.csv', 'quarter2.csv', 'quarter3.csv', 'quarter4.csv']


def sales_counter(filename: str) -> Counter:
    with open(filename, encoding='utf-8') as fi:
        _, *products = csv.reader(fi)
        products_count = Counter()
        for product in products:
            name, *total_count = product
            products_count.update({name: sum(map(int, total_count))})
    return products_count


with open('prices.json', encoding='utf-8') as js:
    prices = json.load(js)

counter = Counter()

for quarter in QUARTERS:
    counter.update(sales_counter(quarter))

total_earned = 0
for product in counter:
    total_earned += counter[product] * prices[product]

print(total_earned)
