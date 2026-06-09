from collections import Counter

counts = Counter(input().split(','))
max_len = max(len(key) for key in counts)
for key in sorted(counts):
    cost = sum(ord(c) for c in key if c.isalpha())
    key_count = counts[key]
    print(f'{key:{max_len}}: {cost} UC x {key_count} = {cost * key_count} UC')

# course solution
from collections import Counter


def get_price(product):
    return sum(map(ord, filter(str.isalpha, product)))


products = Counter(input().split(','))
pattern = '{}: {} UC x {} = {} UC'
spaces = max(map(len, products))

for product, count in sorted(products.items()):
    price = get_price(product)
    total = price * count
    product = product.ljust(spaces, ' ')
    print(pattern.format(product, price, count, total))
