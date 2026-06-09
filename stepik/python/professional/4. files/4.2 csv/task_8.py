import csv

districts = {}
with open('wifi.csv', encoding='utf-8') as file:
    for row in csv.DictReader(file, delimiter=';'):
        district, count = row['district'], int(row['number_of_access_points'])
        districts[district] = districts.get(district, 0) + count


districts = sorted(districts.items(), key=lambda item: (-item[1], item[0]))
for district in districts:
    print(f'{district[0]}: {district[1]}')