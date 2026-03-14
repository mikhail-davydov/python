# Алгоритмы и структуры данных

## Описание

Учебная коллекция реализаций классических алгоритмов и структур данных на Python. Предназначена для изучения основ Computer Science и отработки навыков программирования.

## Реализованные алгоритмы

### Поиск на графах

| Алгоритм | Файл | Описание |
|----------|------|-----------|
| BFS | [`bfs.py`](bfs.py) | Поиск в ширину (Breadth-First Search) — обход графа уровень за уровнем |
| DFS | [`dfs.py`](dfs.py) | Поиск в глубину (Depth-First Search) — рекурсивный обход графа |

### Сортировка

| Алгоритм | Файл | Описание |
|----------|------|-----------|
| Quicksort | [`quicksort.py`](quicksort.py) | Быстрая сортировка с использованием partition |

### Динамическое программирование

| Алгоритм | Файл | Описание |
|----------|------|-----------|
| Fibonacci | [`fibonacci.py`](fibonacci.py) | Вычисление чисел Фибоначчи различными методами |
| Knapsack | [`knapsack.py`](knapsack.py) | Задача о рюкзаке — оптимальный выбор предметов |

## Использование

Импорт и использование алгоритмов:

```python
from algorithms.bfs import bfs
from algorithms.dfs import dfs
from algorithms.fibonacci import fibonacci
from algorithms.knapsack import knapsack
from algorithms.quicksort import quicksort
```

## Запуск тестов

Каждый модуль содержит встроенные примеры использования, которые можно запустить напрямую:

```bash
cd algorithms
python bfs.py
python dfs.py
python fibonacci.py
python knapsack.py
python quicksort.py
```

## Сложность алгоритмов

| Алгоритм | Временная сложность | Пространственная сложность |
|----------|---------------------|---------------------------|
| BFS | O(V + E) | O(V) |
| DFS | O(V + E) | O(V) |
| Quicksort (avg) | O(n log n) | O(log n) |
| Quicksort (worst) | O(n²) | O(n) |
| Fibonacci (naive) | O(2ⁿ) | O(n) |
| Fibonacci (DP) | O(n) | O(n) |
| Knapsack | O(nW) | O(nW) |

Где V — вершины, E — рёбра, n — количество элементов, W — вместимость рюкзака.