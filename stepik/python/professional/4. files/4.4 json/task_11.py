import csv
import json

with open('playgrounds.csv', encoding='utf8') as f_in:
    playgrounds: list[dict] = list(csv.DictReader(f_in, delimiter=';'))
    # print(playgrounds)

addresses = {}
for pg in playgrounds:
    obj_name, key_adm, key_district, value = pg.values()
    # print(key_adm, key_district, value)
    district = addresses.get(key_adm, {})
    district.setdefault(key_district, []).append(value)
    addresses[key_adm] = district

# print(addresses)

with open('addresses.json', 'w', encoding='utf8') as f_out:
    json.dump(addresses, f_out, ensure_ascii=False, indent=3)