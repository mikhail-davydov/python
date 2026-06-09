import csv

with open('sales.csv', 'r', encoding='utf-8') as csv_file:
    reader = csv.DictReader(csv_file, delimiter=';')
    for row in filter(lambda row: int(row['old_price']) > int(row['new_price']), reader):
        print(row['name'])
