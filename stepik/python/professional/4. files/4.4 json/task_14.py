import csv
import json

students = {}
with open('exam_results.csv', encoding='utf8') as f_in:
    reader = csv.DictReader(f_in)
    for row in reader:
        if row['email'] not in students:
            students[row['email']] = row
            students[row['email']]['best_score'] = int(row['score'])
            del students[row['email']]['score']
        elif int(row['score']) >= students[row['email']]['best_score'] and row['date_and_time'] > students[row['email']]['date_and_time']:
            students[row['email']]['best_score'] = int(row['score'])
            students[row['email']]['date_and_time'] = row['date_and_time']

students_sorted = list(map(lambda item: item[1], sorted(students.items(), key=lambda item: item[0])))
# print(students_sorted)

with open('best_scores.json', 'w') as f_out:
    json.dump(students_sorted, f_out, indent=3)