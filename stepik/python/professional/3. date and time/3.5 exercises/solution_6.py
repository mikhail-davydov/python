from datetime import datetime
from collections import defaultdict

# Ввод количества сотрудников
n = int(input())

# Словарь для подсчета количества рождений по датам
birthdays = defaultdict(int)

# Чтение данных о сотрудниках
for _ in range(n):
    line = input().strip()
    name, surname, date_str = line.rsplit(' ', 2)
    birthdays[date_str] += 1

# Нахождение максимального количества рождений в один день
max_count = max(birthdays.values())

# Сбор всех дат с максимальным количеством рождений
max_birthday_dates = []
for date_str, count in birthdays.items():
    if count == max_count:
        max_birthday_dates.append(datetime.strptime(date_str, '%d.%m.%Y'))

# Сортировка дат по возрастанию
max_birthday_dates.sort()

# Вывод результата в требуемом формате
for date in max_birthday_dates:
    print(date.strftime('%d.%m.%Y'))
