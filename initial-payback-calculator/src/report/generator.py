from typing import Dict

from tabulate import tabulate

from src.core.config import TABLE_FORMAT, DAYS_IN_MONTH
from src.core.models import RentalIncome, InitialData


def display_report(
        commercial_space_info: InitialData,
        expenses: float,
        rental_income: RentalIncome,
        shelves_data: Dict[str, float],
        payback_period: tuple
):
    """Выводит результаты на экран."""

    # Получаем список всех полей room_info для полного вывода
    input_data = [(attr, getattr(commercial_space_info, attr)) for attr in dir(commercial_space_info) if
                  not callable(getattr(commercial_space_info, attr)) and not attr.startswith("__")]

    # Таблица с вводными параметрами
    print("\nВходные данные:")
    print(tabulate(input_data, headers=["Параметр", "Значение"], tablefmt=TABLE_FORMAT, numalign="right"))

    # Таблицы с основными результатами
    print("\nРезультаты расчета:")

    print("\nРасход:")
    outcome_table = [
        ["Расходы в месяц:", expenses],
        ["Расходы в день:", round(expenses / DAYS_IN_MONTH, 2)],
    ]
    print(tabulate(outcome_table, headers=["Показатель", "Значение"], tablefmt=TABLE_FORMAT, numalign="right"))

    print("\nРасход детали:")
    total_sales = commercial_space_info.shelf_sales_mean_value_per_month * shelves_data["total_shelves"]
    equiring = total_sales * commercial_space_info.equiring_rate_decimal()
    outcome_details_table = [
        ["Аренда:", commercial_space_info.rent_cost],
        ["Коммунальные услуги:", commercial_space_info.utilities_cost],
        ["Сотрудники:", commercial_space_info.workers_cost],
        ["Эквайринг:", equiring],
        ["Ремонт и доп расходы:", commercial_space_info.initial_investment],
    ]
    print(tabulate(outcome_details_table, headers=["Показатель", "Значение"], tablefmt=TABLE_FORMAT, numalign="right"))

    print("\nПриход:")
    income_table = [
        ["Полная загрузка (до налога)", rental_income.full_load_before_taxes],
        ["Полная загрузка (после налога)", rental_income.full_load_after_taxes],
        ["Частичная загрузка (до налога)", rental_income.partial_load_before_taxes],
        ["Частичная загрузка (после налога)", rental_income.partial_load_after_taxes],
    ]
    print(tabulate(income_table, headers=["Показатель", "Значение"], tablefmt=TABLE_FORMAT, numalign="right"))

    print("\nПриход детали:")
    income_details_table = [
        ["Аренда полок", commercial_space_info.shelf_cost_per_month * shelves_data["total_shelves"]],
        ["Комиссия с продаж", total_sales * commercial_space_info.sales_rate_decimal() - equiring],
        ["Дополнительный доход", commercial_space_info.additional_expected_income_per_month],
    ]
    print(tabulate(income_details_table, headers=["Показатель", "Значение"], tablefmt=TABLE_FORMAT, numalign="right"))

    print("\nЧистая прибыль:")
    profit_table = [
        ["Полная загрузка (до налога)", rental_income.full_load_before_taxes - expenses],
        ["Полная загрузка (после налога)", rental_income.full_load_after_taxes - expenses],
        ["Частичная загрузка (до налога)", rental_income.partial_load_before_taxes - expenses],
        ["Частичная загрузка (после налога)", rental_income.partial_load_after_taxes - expenses],
    ]
    print(tabulate(profit_table, headers=["Показатель", "Значение"], tablefmt=TABLE_FORMAT, numalign="right"))

    print("\nСроки окупаемости:")
    payback_table = [
        ["Срок окупаемости (полная загрузка, мес.)", round(payback_period[0])],
        ["Срок окупаемости (частичная загрузка, мес.)", round(payback_period[1])],
    ]
    print(tabulate(payback_table, headers=["Показатель", "Значение"], tablefmt=TABLE_FORMAT, numalign="right"))

    print("\nДополнительная информация:")
    additions_table = [
        ["Общее количество полок:", shelves_data["total_shelves"]],
        ["Общее количество стеллажей:", shelves_data["horizontal_shelves_count"]],
        ["Количество полок в высоту:", shelves_data["vertical_shelves_count"]],
        ["Площадь, занятая полками:", shelves_data["total_shelves_area"]],
        ["Свободная площадь:", commercial_space_info.total_area - shelves_data["total_shelves_area"]],
    ]
    print(tabulate(additions_table, headers=["Показатель", "Значение"], tablefmt=TABLE_FORMAT, numalign="right"))
