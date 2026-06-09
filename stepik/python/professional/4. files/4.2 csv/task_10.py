import csv
from datetime import datetime

# Словарь для хранения последней записи по email
latest_records = {}

date_format = "%d/%m/%Y %H:%M"

# Чтение исходного файла
with open("name_log.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        email = row['email']
        current_dtime = datetime.strptime(row['dtime'], date_format)
        
        # Если email еще не встречался или найдена более свежая запись
        if email not in latest_records:
            latest_records[email] = row
        else:
            existing_dtime = datetime.strptime(latest_records[email]['dtime'], date_format)
            if current_dtime > existing_dtime:
                latest_records[email] = row

# Сортировка по email и запись в новый файл
sorted_records = sorted(latest_records.values(), key=lambda x: x['email'])

with open("new_name_log.csv", "w", encoding="utf-8", newline="") as file:
    fieldnames = ['username', 'email', 'dtime']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(sorted_records)