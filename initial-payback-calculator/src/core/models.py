from dataclasses import dataclass
from typing import NamedTuple

from src.core.config import DAYS_IN_MONTH, WEEKS_IN_MONTH


@dataclass
class InitialData:
    """Класс хранит информацию о помещении."""
    square_meter_cost: float | None = None
    total_area: float | None = None
    monthly_rent: float | None = None
    utilities_cost: float | None = None
    ceiling_height: float | None = None
    wall_length: float | None = None
    shelf_max_height: float | None = None
    shelf_width: float | None = None
    shelf_depth: float | None = None
    shelf_height: float | None = None
    shelf_cost_per_week: float | None = None
    workers_count: int | None = None
    worker_change_cost: float | None = None
    worker_tax_rate: float | None = None
    equiring_rate: float | None = None
    tax_rate: float | None = None
    initial_investment: float | None = None
    sales_rate: float | None = None
    shelf_sales_mean_value_per_month: float | None = None
    additional_expected_income_per_month: float | None = None

    @property
    def shelf_cost_per_month(self):
        if self.shelf_cost_per_week is not None and self.shelf_cost_per_week > 0:
            return self.shelf_cost_per_week * WEEKS_IN_MONTH
        return 0

    @property
    def rent_cost(self):
        """Возвращает арендную плату за помещение"""
        if self.monthly_rent is not None and self.monthly_rent > 0:
            return self.monthly_rent
        elif self.square_meter_cost is not None and self.total_area is not None:
            return self.square_meter_cost * self.total_area
        return 0

    @property
    def workers_cost(self):
        """Возвращает месячную зарплату сотрудников"""
        if self.workers_count is not None and self.worker_change_cost is not None:
            return self.workers_count * self.worker_change_cost * self.worker_tax_rate_decimal() * DAYS_IN_MONTH
        return 0

    def tax_rate_decimal(self):
        """Преобразует налоговую ставку в дробный вид"""
        return self.tax_rate / 100 if self.tax_rate is not None else 0

    def sales_rate_decimal(self):
        """Преобразует ставку с продаж в дробный вид"""
        return self.sales_rate / 100 if self.sales_rate is not None else 0

    def worker_tax_rate_decimal(self):
        """Преобразует ставку налога на работника в дробный вид"""
        return (1 + self.worker_tax_rate / 100) if self.worker_tax_rate is not None else 1

    def equiring_rate_decimal(self):
        """Преобразует ставку эквайринга' в дробный вид"""
        return self.equiring_rate / 100 if self.equiring_rate is not None else 0


class RentalIncome(NamedTuple):
    """Хранит доходы от аренды полок до и после налогов."""
    full_load_before_taxes: float
    full_load_after_taxes: float
    partial_load_before_taxes: float
    partial_load_after_taxes: float
