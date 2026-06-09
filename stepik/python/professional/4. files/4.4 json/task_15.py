import json

with open('food_services.json', encoding='utf-8') as file:
    data = json.load(file)

district_count = {}
network_count = {}

for place in data:
    district = place['District']
    district_count[district] = district_count.get(district, 0) + 1

    if place['OperatingCompany']:
        network = place['OperatingCompany']
        network_count[network] = network_count.get(network, 0) + 1

max_district = max(district_count.items(), key=lambda x: x[1])
max_network = max(network_count.items(), key=lambda x: x[1])

print(f'{max_district[0]}: {max_district[1]}')
print(f'{max_network[0]}: {max_network[1]}')
