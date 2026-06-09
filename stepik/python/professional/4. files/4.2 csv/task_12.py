import csv

# Считываем данные из исходного файла
with open('student_counts.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    headers = next(reader)  # Считываем заголовки
    rows = list(reader)     # Считываем все строки

# Извлекаем год (первый столбец) и классы (остальные столбцы)
year_column = headers[0]
class_columns = headers[1:]

# Сортируем классы по номеру, затем по букве
# Класс в формате "<номер>-<буква>"
sorted_class_columns = sorted(class_columns, key=lambda x: (int(x.split('-')[0]), x.split('-')[1]))

# Формируем новые заголовки
new_headers = [year_column] + sorted_class_columns

# Записываем отсортированные данные в новый файл
with open('sorted_student_counts.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    # Записываем отсортированные данные в новый файл
    writer.writerow(new_headers)
    
    # Перезаписываем строки, соответствующие отсортированным заголовкам
    for row in rows:
        year = row[0]
        # Создаем словарь из исходных данных строки
        data = dict(zip(headers[1:], row[1:]))
        # Формируем новую строку в порядке отсортированных классов
        sorted_row = [data[class_name] for class_name in sorted_class_columns]
        # Записываем год и отсортированные данные
        writer.writerow([year] + sorted_row)
