func = input()
a, b = map(int, input().split())
expressions = [eval(func) for x in range(a, b + 1)]

print(f'Минимальное значение функции {func} на отрезке [{a}; {b}] равно {min(expressions)}')
print(f'Максимальное значение функции {func} на отрезке [{a}; {b}] равно {max(expressions)}')