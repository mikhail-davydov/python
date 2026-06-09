from datetime import datetime, timedelta

current_date_str = input().strip()
n = int(input().strip())

# Преобразуем текущую дату
current_date = datetime.strptime(current_date_str, "%d.%m.%Y")

# Определяем диапазон ближайших 7 дней (включая завтра, исключая сегодня)
next_week = [(current_date + timedelta(days=i)).strftime("%d.%m") for i in range(1, 8)]

# Список для хранения подходящих сотрудников
candidates = []

current_year = current_date.year

for _ in range(n):
    line = input().strip().split()
    name = line[0]
    surname = line[1]
    birth_date_str = line[2]
    
    # Преобразуем дату рождения
    birth_date = datetime.strptime(birth_date_str, "%d.%m.%Y")
    birth_date_this_year = birth_date.replace(year=current_year)
    
    # Проверяем, попадает ли день рождения в ближайшие 7 дней
    if birth_date_this_year.strftime("%d.%m") in next_week:
        # Сохраняем имя, фамилию и оригинальную дату рождения для сортировки по возрасту
        candidates.append((name, surname, birth_date))

# Если есть подходящие сотрудники, находим самого молодого (максимальная дата рождения)
if candidates:
    # Сортируем по дате рождения по убыванию и выбираем первого
    youngest = max(candidates, key=lambda x: x[2])
    print(f"{youngest[0]} {youngest[1]}")
else:
    print("Дни рождения не планируются")