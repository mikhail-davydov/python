from datetime import datetime, timedelta

# Считываем входные даты
start_date = datetime.strptime(input().strip(), "%d.%m.%Y")
end_date = datetime.strptime(input().strip(), "%d.%m.%Y")

# Находим первую дату с нечетной суммой дня и месяца
current = start_date
while current <= end_date:
    if (current.day + current.month) % 2 == 1:
        break
    current += timedelta(days=1)

# Перебираем каждую третью дату, начиная с найденной
while current <= end_date:
    # Проверяем, что день недели не понедельник (0) и не четверг (3)
    if current.weekday() != 0 and current.weekday() != 3:
        print(current.strftime("%d.%m.%Y"))

    # Переход к каждой третьей дате
    current += timedelta(days=3)
