from datetime import datetime

fmt = '%d.%m.%Y'
employees = []
for _ in range(int(input())):
    fn, ln, dob = input().split()
    employees.append((fn, ln, datetime.strptime(dob, fmt)))

# Find the oldest date of birth
oldest_dob = min(employee[2] for employee in employees)

# Count how many employees have the oldest date of birth
oldest_employees = [emp for emp in employees if emp[2] == oldest_dob]

# If there's only one oldest employee, output their info
if len(oldest_employees) == 1:
    employee = oldest_employees[0]
    print(f"{oldest_dob.strftime(fmt)} {employee[0]} {employee[1]}")
else:
    # If multiple employees share the oldest date, output the date and count
    print(f"{oldest_dob.strftime(fmt)} {len(oldest_employees)}")