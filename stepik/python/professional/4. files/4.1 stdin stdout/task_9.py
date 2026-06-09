import sys


def detect_progression(numbers):
    if len(numbers) < 3:
        print("Не прогрессия")
        return

    # Проверка на арифметическую прогрессию
    is_arithmetic = True
    diff = numbers[1] - numbers[0]
    for i in range(2, len(numbers)):
        if numbers[i] - numbers[i - 1] != diff:
            is_arithmetic = False
            break

    if is_arithmetic:
        print("Арифметическая прогрессия")
        return

    # Проверка на геометрическую прогрессию
    is_geometric = True
    if numbers[0] == 0:
        print("Не прогрессия")
        return

    if numbers[1] % numbers[0] != 0:
        is_geometric = False
    else:
        ratio = numbers[1] // numbers[0]
        for i in range(2, len(numbers)):
            if numbers[i - 1] == 0 or numbers[i] % numbers[i - 1] != 0 or numbers[i] // numbers[i - 1] != ratio:
                is_geometric = False
                break

    if is_geometric:
        print("Геометрическая прогрессия")
    else:
        print("Не прогрессия")


numbers = [int(line.strip()) for line in sys.stdin if line.strip()]
detect_progression(numbers)
