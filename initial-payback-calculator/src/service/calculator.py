from typing import Dict

from src.core.config import PARTIAL_LOAD_RATIO, STARTING_INCOME_RATIO, INCOME_INCREMENT_STEP
from src.core.models import InitialData, RentalIncome


def calculate_monthly_expenses(commercial_space_info: InitialData) -> Dict[str, float]:
    """Рассчитывает общие ежемесячные расходы."""
    rent_cost = commercial_space_info.rent_cost
    utilities_cost = commercial_space_info.utilities_cost or 0
    workers_cost = commercial_space_info.workers_cost

    total_expenses = rent_cost + utilities_cost + workers_cost
    return {"total_expenses": total_expenses}


def calculate_shelves_and_area(commercial_space_info: InitialData) -> Dict[str, float]:
    """Рассчитывает возможные показатели размещения полок."""
    max_available_height = min(commercial_space_info.ceiling_height, commercial_space_info.shelf_max_height)
    vertical_shelves_count = max_available_height // commercial_space_info.shelf_height
    horizontal_shelves_count = commercial_space_info.wall_length // commercial_space_info.shelf_width
    single_shelf_area = commercial_space_info.shelf_width * commercial_space_info.shelf_depth

    total_shelves = vertical_shelves_count * horizontal_shelves_count
    total_shelves_area = single_shelf_area * horizontal_shelves_count
    return {
        "total_shelves": total_shelves,
        "horizontal_shelves_count": horizontal_shelves_count,
        "vertical_shelves_count": vertical_shelves_count,
        "total_shelves_area": total_shelves_area
    }


def calculate_rental_income(commercial_space_info: InitialData, total_shelves: int) -> RentalIncome:
    """Рассчитывает потенциальный доход от аренды полок + процент с продаж + ожидаемый дополнительный доход."""
    sales_total = commercial_space_info.shelf_sales_mean_value_per_month * total_shelves
    equiring = sales_total * commercial_space_info.equiring_rate_decimal()
    tax_rate = commercial_space_info.tax_rate_decimal()

    full_load_revenue = (
            total_shelves * commercial_space_info.shelf_cost_per_month +
            sales_total * commercial_space_info.sales_rate_decimal() - equiring +
            commercial_space_info.additional_expected_income_per_month
    )
    full_load_after_taxes = full_load_revenue * (1 - tax_rate)

    partial_load_revenue = full_load_revenue * PARTIAL_LOAD_RATIO
    partial_load_after_taxes = partial_load_revenue * (1 - tax_rate)

    return RentalIncome(
        full_load_before_taxes=full_load_revenue,
        full_load_after_taxes=full_load_after_taxes,
        partial_load_before_taxes=partial_load_revenue,
        partial_load_after_taxes=partial_load_after_taxes
    )


def calculate_payback_period(
        commercial_space_info: InitialData,
        rental_income: RentalIncome,
        expenses: float
) -> tuple:
    """
    Рассчитывает срок окупаемости вложений для полной и частичной загрузки.
    Возвращает кортеж (payback_full_load, payback_partial_load).
    """

    # Формирование начальной суммы инвестирования
    initial_payment = (commercial_space_info.rent_cost + commercial_space_info.utilities_cost) * 2.5
    initial_investment = commercial_space_info.initial_investment + initial_payment
    # initial_investment = commercial_space_info.repair_cost + 2 * expenses

    # Текущие значения дохода для полной и частичной загрузки
    current_income_full_load = rental_income.full_load_after_taxes * STARTING_INCOME_RATIO
    current_income_partial_load = rental_income.partial_load_after_taxes * STARTING_INCOME_RATIO

    # Переменные для хранения количества месяцев и накопленных платежей
    months_full_load = 0
    months_partial_load = 0
    accumulated_payment_full_load = 0
    accumulated_payment_partial_load = 0

    # Цикл вычисления периода окупаемости для полной загрузки
    while accumulated_payment_full_load < initial_investment:
        # Чистый доход за месяц при полной загрузке
        net_profit_full_load = current_income_full_load - expenses

        # Увеличение общего дохода
        accumulated_payment_full_load += net_profit_full_load

        # Переход к следующему месяцу
        months_full_load += 1

        # Повышаем доход на заданный шаг, ограничиваясь максимальным уровнем (100%)
        current_income_full_load += rental_income.full_load_after_taxes * INCOME_INCREMENT_STEP
        if current_income_full_load > rental_income.full_load_after_taxes:
            current_income_full_load = rental_income.full_load_after_taxes

    # Аналогично считаем период окупаемости для частичной загрузки
    while accumulated_payment_partial_load < initial_investment:
        # Чистый доход за месяц при частичной загрузке
        net_profit_partial_load = current_income_partial_load - expenses

        # Увеличение общего дохода
        accumulated_payment_partial_load += net_profit_partial_load

        # Переход к следующему месяцу
        months_partial_load += 1

        # Повышаем доход на заданный шаг, ограничиваясь максимумом (70%)
        current_income_partial_load += rental_income.partial_load_after_taxes * INCOME_INCREMENT_STEP
        if current_income_partial_load > rental_income.partial_load_after_taxes:
            current_income_partial_load = rental_income.partial_load_after_taxes

    return months_full_load, months_partial_load
