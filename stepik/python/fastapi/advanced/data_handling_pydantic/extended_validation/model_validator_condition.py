from typing import Optional

from pydantic import BaseModel, ValidationError, model_validator


class Request(BaseModel):
    status: str
    reason: Optional[str] = None

    @model_validator(mode='after')
    def check_reason_for_rejected(self):
        if self.status == 'rejected' and self.reason is None:
            raise ValueError('При статусе "rejected" поле "reason" является обязательным.')
        if self.status != 'rejected' and self.reason is not None:
            raise ValueError('Поле "reason" должно быть пустым, если статус не "rejected".')
        return self


if __name__ == '__main__':

    # Демонстрация успешной валидации
    try:
        req1 = Request(status="approved")
        print(f"Успех: {req1}")
        req2 = Request(status="rejected", reason="Insufficient data")
        print(f"Успех: {req2}")
    except ValidationError as e:
        print(f"Ошибка: {e}")

    # Демонстрация ошибок
    try:
        Request(status="rejected")  # Нет причины при reject
    except ValidationError as e:
        print(f"\nОшибка валидации: {e}")

    try:
        Request(status="approved", reason="No reason needed")  # Причина при approved
    except ValidationError as e:
        print(f"\nОшибка валидации: {e}")
