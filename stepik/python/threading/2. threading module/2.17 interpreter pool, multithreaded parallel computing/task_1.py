# python 3.14

import concurrent.futures
from concurrent.futures import ThreadPoolExecutor, InterpreterPoolExecutor, ProcessPoolExecutor, Executor
import random
import time
import os


def calculate_pi_monte_carlo(i):
    """
    Вычисляет число Пи методом Монте-Карло.

    Параметры:
    i (int): Номер вычисления.

    Возвращает:
    tuple: Номер вычисления, число Пи.
    """
    series = 10**6  # Количество случайных точек для генерации
    inside_circle = 0  # Счетчик точек, попавших внутрь единичного круга

    # Генерация случайных точек и подсчет попавших в круг
    for _ in range(series):
        x = random.uniform(-1, 1)  # Генерация случайной координаты x
        y = random.uniform(-1, 1)  # Генерация случайной координаты y
        if x**2 + y**2 <= 1:  # Проверка, находится ли точка внутри круга
            inside_circle += 1  # Увеличиваем счетчик, если точка внутри круга

    # Расчет числа Пи
    pi_estimate = (inside_circle / series) * 4
    return i, pi_estimate


def get_total_memory_usage():
    import psutil
    """Возвращает общее использование памяти всеми процессами: основной + дочерние (если есть)"""
    current_process = psutil.Process(os.getpid())
    children = current_process.children(recursive=True)  # все дочерние процессы
    total_memory = current_process.memory_info().rss / 1024  # память основного процесса
    for child in children:
        total_memory += child.memory_info().rss / 1024  # память дочерних процессов
    return total_memory


def main(executor: concurrent.futures.Executor):
    start_time = time.perf_counter()
    peak_memory = 0
    with executor() as pool:
        results = pool.map(calculate_pi_monte_carlo, range(1, 5))
        for i, result in results:
            print(f"Вычиcление №{i}. Число Пи={result:.6f}")
            current_memory = get_total_memory_usage()
            if current_memory > peak_memory:
                peak_memory = current_memory
    print(f"Пул {pool.__class__.__name__} выполнил расчет за {time.perf_counter()-start_time:.3f}c.")
    print(f"Пиковое использование памяти: {peak_memory:.2f} KB\n")


if __name__ == '__main__':
    for executor in (ThreadPoolExecutor, InterpreterPoolExecutor, ProcessPoolExecutor):
        main(executor)