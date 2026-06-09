import json

with open('countries.json', encoding='utf8') as f_in:
    data: list[dict] = json.load(f_in)
    # print(data)

religions = {}
for item in data:
    key = item['religion']
    value = item['country']
    religions[key] = religions.get(key, []) + [value]

# print(religions)

with open('religion.json', 'w') as f_out:
    json.dump(religions, f_out)