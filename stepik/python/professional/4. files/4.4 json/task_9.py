import json

with open('people.json', encoding='utf8') as f_in:
    data: list[dict] = json.load(f_in)
    # print(data)

keys_set = set([key for elem in data for key in elem.keys()])
# print(keys_set)

for key_name in keys_set:
    for elem in data:
        elem.setdefault(key_name, None)
# print(data)

with open('updated_people.json', 'w', encoding='utf8') as f_out:
    json.dump(data, f_out)