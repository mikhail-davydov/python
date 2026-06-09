import json

with open('food_services.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

max_seats_by_type = {}

for establishment in data:
    type_object = establishment['TypeObject']
    seats_count = establishment['SeatsCount']
    name = establishment['Name']

    if type_object not in max_seats_by_type or seats_count > max_seats_by_type[type_object]['SeatsCount']:
        max_seats_by_type[type_object] = {
            'Name': name,
            'SeatsCount': seats_count
        }

for type_object in sorted(max_seats_by_type.keys()):
    info = max_seats_by_type[type_object]
    print(f'{type_object}: {info["Name"]}, {info["SeatsCount"]}')
