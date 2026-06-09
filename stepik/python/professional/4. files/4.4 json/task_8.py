import json

with open('data1.json', encoding='utf8') as file1, open('data2.json', encoding='utf8') as file2:
    data1: dict = json.load(file1)
    data2: dict = json.load(file2)

# print(data1)
# print(data2)

data1.update(data2)

# print(data1)

with open('data_merge.json', 'w', encoding='utf8') as out:
    json.dump(data1, out)
