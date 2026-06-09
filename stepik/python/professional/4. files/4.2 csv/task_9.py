import csv

male = []
female = []
with open('titanic.csv', encoding='utf-8') as file:
    data = filter(lambda row: int(row['survived']) and float(row['age']) < 18, csv.DictReader(file, delimiter=';'))
    for row in data:
        name = row['name']
        male.append(name) if row['sex'] == 'male' else female.append(name)

common = male + female
print(*common, sep='\n')
