from collections import Counter


def print_bar_chart(data, mark):
    counts = Counter(data)
    max_len = max(map(len, counts))
    for key, count in counts.most_common():
        print(f'{key:{max_len}} |{mark * count}')


languages = ['java', 'java', 'python', 'C++', 'assembler', 'java', 'C++', 'C', 'pascal', 'C++', 'pascal', 'java']

print_bar_chart(languages, '#')
