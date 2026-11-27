from datetime import datetime

from pydantic import BaseModel, ValidationError, model_validator


class Event(BaseModel):
    name: str
    start_date: datetime
    end_date: datetime

    @model_validator(mode='after')
    def check_dates_order(self):
        if self.start_date and self.end_date and self.start_date > self.end_date:
            raise ValueError('Дата начала не может быть позже даты окончания')
        return self  # Всегда возвращаем self


if __name__ == '__main__':

    # Демонстрация успешной валидации
    try:
        event1 = Event(name="Conference", start_date="2025-01-10T09:00:00", end_date="2025-01-12T17:00:00")
        print(f"Успех: {event1}")
    except ValidationError as e:
        print(f"Ошибка: {e}")

    # Демонстрация ошибки
    try:
        Event(name="Meeting", start_date="2025-02-15T10:00:00", end_date="2025-02-14T11:00:00")
    except ValidationError as e:
        print(f"\nОшибка валидации: {e}")
