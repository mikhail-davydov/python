import sys


def print_results(heights):
    if not heights:
        print('нет учеников')
        return
    min_h = min(heights)
    max_h = max(heights)
    avg_h = sum(heights) / len(heights)
    print(f'Рост самого низкого ученика: {min_h}')
    print(f'Рост самого высокого ученика: {max_h}')
    print(f'Средний рост: {avg_h}')


heights = [int(line.strip()) for line in sys.stdin if line.strip()]
print_results(heights)
