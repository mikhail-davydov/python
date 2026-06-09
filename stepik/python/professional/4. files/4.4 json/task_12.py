import csv
import json

with open('students.json', encoding='utf-8') as f_in:
    data = json.load(f_in)

students = [
    {'name': student['name'], 'phone': student['phone']}
    for student in data
    if student['age'] >= 18 and student['progress'] >= 75
]

students.sort(key=lambda s: s['name'])

# for student in students:
#     print(student)

with open('data.csv', 'w', newline='', encoding='utf-8') as f_out:
    writer = csv.DictWriter(f_out, fieldnames=['name', 'phone'])
    writer.writeheader()
    writer.writerows(students)
