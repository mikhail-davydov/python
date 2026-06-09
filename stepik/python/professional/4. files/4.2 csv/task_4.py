import csv

agg_data = {}
with open('salary_data.csv', encoding='utf-8') as csv_file:
    data = list(csv.DictReader(csv_file, delimiter=';'))
    company_set = set([row['company_name'] for row in data])
    for company in company_set:
        filtered_by_company = list(filter(lambda row: row['company_name'] == company, data))
        agg_data[company] = sum(map(lambda row: int(row['salary']), filtered_by_company)) / len(filtered_by_company)

company_name_sorted_list = list(map(lambda x: x[0], sorted(agg_data.items(), key=lambda item: (item[1], item[0]))))
print(*company_name_sorted_list, sep='\n')
