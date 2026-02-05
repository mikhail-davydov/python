from src.core.models import InitialData
from src.report.generator import display_report
from src.service.calculator import calculate_monthly_expenses, calculate_rental_income, calculate_payback_period, \
    calculate_shelves_and_area
from src.service.reader import load_json
from src.service.validator import validate_commercial_space_info


def main():
    # Путь к файлу JSON
    file_path = '.private/initial-data.json'

    # Загружаем данные из JSON файла
    raw_data = load_json(file_path)

    # Создаем экземпляр класса и наполняем его данными
    initial_data = InitialData(**raw_data)

    # Проверка правильности введённых данных
    validation_errors = validate_commercial_space_info(initial_data)
    if validation_errors:
        print("Некорректные данные:")
        print("\n".join(validation_errors))
        return

    # Подсчет месячных расходов
    expenses = calculate_monthly_expenses(initial_data)["total_expenses"]

    # Подсчет возможных показателей размещения полок
    shelves_data = calculate_shelves_and_area(initial_data)
    total_shelves = shelves_data["total_shelves"]

    # Подсчет дохода от аренды
    rental_income = calculate_rental_income(initial_data, total_shelves)

    # Подсчет срока окупаемости
    payback_period = calculate_payback_period(initial_data, rental_income, expenses)

    # Вывод результатов
    display_report(initial_data, expenses, rental_income, shelves_data, payback_period)


if __name__ == "__main__":
    main()
