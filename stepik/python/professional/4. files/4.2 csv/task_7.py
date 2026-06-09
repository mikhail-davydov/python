import csv

domains = {}
with open('data.csv', encoding='utf-8') as read_file:
    rows = csv.DictReader(read_file)
    for row in rows:
        domain = row['email'].split('@')[-1]
        domains[domain] = domains.get(domain, 0) + 1

domains = sorted(domains.items(), key=lambda item: ([item[1], item[0]]))

columns = ['domain', 'count']
with open('domain_usage.csv', 'w', encoding='utf-8', newline='') as write_file:
    writer = csv.writer(write_file)
    writer.writerow(columns)
    writer.writerows(domains)