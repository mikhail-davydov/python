from datetime import datetime

# Формат ввода и дата выхода курса
format = "%d.%m.%Y %H:%M"
date_target = datetime.strptime("08.11.2022 12:00", format)

# Ввод текущей даты и времени
input_date_str = input().strip()
current_date = datetime.strptime(input_date_str, format)

# Проверка, не вышел ли курс уже
if current_date >= date_target:
    print("Курс уже вышел!")
else:
    # Разница во времени
    delta = date_target - current_date
    total_minutes = int(delta.total_seconds() // 60)
    days = total_minutes // (24 * 60)
    hours = (total_minutes % (24 * 60)) // 60
    minutes = total_minutes % 60

    # Функция для склонения существительных
    def plural_form(n, forms):
        # forms = [один, два, пять]
        # Пример: ["день", "дня", "дней"]
        if n % 100 in [11, 12, 13, 14]:
            return forms[2]
        elif n % 10 == 1:
            return forms[0]
        elif n % 10 in [2, 3, 4]:
            return forms[1]
        else:
            return forms[2]

    # Формирование результата
    if days > 0:
        # Если есть дни, выводим только дни и часы (минуты игнорируем)
        day_word = plural_form(days, ["день", "дня", "дней"])
        if hours > 0:
            hour_word = plural_form(hours, ["час", "часа", "часов"])
            print(f"До выхода курса осталось: {days} {day_word} и {hours} {hour_word}")
        else:
            print(f"До выхода курса осталось: {days} {day_word}")
    else:
        # Дней нет — выводим часы и/или минуты
        result_parts = []
        if hours > 0:
            hour_word = plural_form(hours, ["час", "часа", "часов"])
            result_parts.append(f"{hours} {hour_word}")
        if minutes > 0:
            minute_word = plural_form(minutes, ["минута", "минуты", "минут"])
            result_parts.append(f"{minutes} {minute_word}")

        if result_parts:
            result_str = " и ".join(result_parts)
            print(f"До выхода курса осталось: {result_str}")
        else:
            print("Курс уже вышел!")  # На случай точного совпадения