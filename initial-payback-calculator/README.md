# Калькулятор начальной окупаемости

## Описание

Инструмент для расчёта сроков окупаемости начальных инвестиций в бизнес по производству handmade-товаров. Позволяет оценить, за какой период времени выручка от продаж покроет первоначальные затраты.

## Назначение

Калькулятор помогает:
- Определить точку безубыточности
- Рассчитать срок возврата инвестиций
- Оценить рентабельность бизнеса
- Планировать финансовые показатели

## Функциональность

### Модули приложения

| Модуль | Файл | Описание |
|--------|------|----------|
| Конфигурация | [`src/core/config.py`](src/core/config.py) | Настройки приложения |
| Модели данных | [`src/core/models.py`](src/core/models.py) | Структуры данных |
| Калькулятор | [`src/service/calculator.py`](src/service/calculator.py) | Логика расчёта окупаемости |
| Валидация | [`src/service/validator.py`](src/service/validator.py) | Проверка входных данных |
| Чтение данных | [`src/service/reader.py`](src/service/reader.py) | Загрузка данных |
| Генератор отчётов | [`src/report/generator.py`](src/report/generator.py) | Формирование отчётов |

## Входные данные

Калькулятор принимает следующие параметры:
- Стоимость материалов на единицу продукции
- Цена продажи единицы продукции
- Объём производства (количество единиц)
- Начальные инвестиции (оборудование, аренда и т.д.)
- Дополнительные регулярные расходы

## Выходные данные

Результаты расчёта включают:
- Выручку от продаж
- Себестоимость продукции
- Прибыль (валовую и чистую)
- Срок окупаемости (в месяцах/единицах продукции)
- Точку безубыточности

## Структура проекта

```
initial-payback-calculator/
├── main.py                  # Точка входа
├── requirements.txt         # Зависимости
├── src/
│   ├── core/
│   │   ├── config.py       # Конфигурация
│   │   └── models.py       # Модели данных
│   ├── service/
│   │   ├── calculator.py   # Логика расчёта
│   │   ├── validator.py   # Валидация
│   │   └── reader.py      # Чтение данных
│   └── report/
│       └── generator.py    # Генератор отчётов
└── v2/                      # Версия 2 (в разработке)
    ├── config/
    ├── models/
    ├── reports/
    └── service/
```

## Установка и запуск

### Требования

- Python 3.10+

### Установка зависимостей

```bash
cd initial-payback-calculator
pip install -r requirements.txt
```

### Запуск

```bash
python main.py
```

## Пример использования

```python
from src.service.calculator import PaybackCalculator
from src.core.models import Product, Investment

# Создание объектов
product = Product(
    material_cost=500,
    selling_price=1500,
    quantity=100
)

investment = Investment(
    initial=50000,
    monthly_expenses=10000
)

# Расчёт
calculator = PaybackCalculator()
result = calculator.calculate(product, investment)

print(f"Срок окупаемости: {result.months} месяцев")
```