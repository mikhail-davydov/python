import calendar

years = [calendar.isleap(int(input())) for _ in range(int(input()))]

print(*years, sep='\n')
