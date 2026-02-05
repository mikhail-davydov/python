from typing import List

from src.core.models import InitialData


def validate_commercial_space_info(initial_data: InitialData) -> List[str]:
    """Проверяет правильность введённых данных."""
    errors = []

    # Проверяем все обязательные численные поля
    numeric_fields = [
        ('square_meter_cost', 'Цена за квадратный метр'),
        ('total_area', 'Общая площадь помещения'),
        ('monthly_rent', 'Ежемесячная аренда'),
        ('utilities_cost', 'Расходы на коммунальные услуги'),
        ('ceiling_height', 'Высота потолков'),
        ('wall_length', 'Полезная длина стен'),
        ('shelf_max_height', 'Максимальная высота полки'),
        ('shelf_width', 'Ширина полки'),
        ('shelf_depth', 'Глубина полки'),
        ('shelf_height', 'Высота полки'),
        ('shelf_cost_per_week', 'Стоимость размещения товара на полке в неделю'),
        ('workers_count', 'Количество работников'),
        ('worker_change_cost', 'Стоимость смены работника'),
        ('worker_tax_rate', 'Налоговая ставка на заработную плату'),
        ('equiring_rate', 'Эквайринговая комиссия'),
        ('tax_rate', 'Налоговая ставка'),
        ('initial_investment', 'Первоначальные вложения'),
        ('sales_rate', 'Комиссия с продаж'),
        ('shelf_sales_mean_value_per_month', 'Средняя выручка с одной полки в месяц'),
        ('additional_expected_income_per_month', 'Дополнительный ожидаемый доход в месяц')
    ]

    for field_name, desc in numeric_fields:
        value = getattr(initial_data, field_name)

        # Проверяем наличие значения и его отрицательность
        if value is None or (isinstance(value, (float, int)) and value < 0):
            errors.append(f'Значение "{desc}" не может быть отрицательным.')

    return errors
