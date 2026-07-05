import multiprocessing

print(f"Количество логических ядер: {multiprocessing.cpu_count()}")
print(f"Список методов запуска процессов: {multiprocessing.get_all_start_methods()}")
