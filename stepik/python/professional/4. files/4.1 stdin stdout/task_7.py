import sys

news = [tuple(line.strip().split(' / ')) for line in sys.stdin]
theme = news.pop()[0]

sorted_news = list(map(lambda x: x[0], sorted(filter(lambda x: x[1] == theme, sorted(news)), key=lambda x: x[2])))

print(*sorted_news, sep='\n')