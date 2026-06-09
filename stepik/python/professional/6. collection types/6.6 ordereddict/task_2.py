from collections import OrderedDict

data = OrderedDict({'Name': 'Брусника', 'IsNetObject': 'да', 'OperatingCompany': 'Брусника', 'TypeObject': 'кафе',
                    'AdmArea': 'Центральный административный округ', 'District': 'район Арбат',
                    'Address': 'город Москва, переулок Сивцев Вражек, дом 6/2', 'SeatsCount': '10'}
                   )

ordered_data = OrderedDict()
iterations = [True if i % 2 else False for i in range(len(data))]
for last in iterations:
    key, value = data.popitem(last)
    ordered_data[key] = value

print(ordered_data)

# course solution
from collections import OrderedDict

data = OrderedDict({'Name': 'Брусника', 'IsNetObject': 'да', 'OperatingCompany': 'Брусника', 'TypeObject': 'кафе',
                    'AdmArea': 'Центральный административный округ', 'District': 'район Арбат',
                    'Address': 'город Москва, переулок Сивцев Вражек, дом 6/2', 'SeatsCount': '10'}
                   )

new_data = OrderedDict()

rule = False
length = len(data)
for _ in range(length):
    key, value = data.popitem(last=rule)
    new_data[key] = value
    rule = not rule

print(new_data)
