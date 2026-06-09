import json

with open('data.json', encoding='utf-8') as file:
    data = json.load(file)

updated = []
for item in data:
    if isinstance(item, str):
        updated.append(item + '!')
    elif isinstance(item, bool):
        updated.append(not item)
    elif isinstance(item, int):
        updated.append(item + 1)
    elif isinstance(item, list):
        updated.append(item * 2)
    elif isinstance(item, dict):
        item['newkey'] = None
        updated.append(item)

with open('updated_data.json', 'w', encoding='utf-8') as file:
    json.dump(updated, file, indent=3)
