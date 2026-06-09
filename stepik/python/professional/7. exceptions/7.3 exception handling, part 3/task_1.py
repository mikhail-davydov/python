import calendar

try:
    num = int(input())
    if num < 1 or num > 12:
        print('Введено число из недопустимого диапазона')
    else:
        print(calendar.month_name[num])
except ValueError:
    print('Введено некорректное значение')
