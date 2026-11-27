from typing import Optional

from pydantic import BaseModel, ValidationError, model_validator


class Comment(BaseModel):
    text: str
    user_id: Optional[int] = None
    guest_name: Optional[str] = None

    @model_validator(mode='after')
    def check_user_or_guest(self):
        if self.user_id is not None and self.guest_name is not None:
            raise ValueError(
                'Комментарий должен быть либо от зарегистрированного пользователя, либо от гостя, но не от обоих сразу.')
        if self.user_id is None and self.guest_name is None:
            raise ValueError('Комментарий должен быть либо от зарегистрированного пользователя, либо от гостя.')
        return self


if __name__ == '__main__':

    # Демонстрация успешной валидации (один из вариантов)
    try:
        comment1 = Comment(text="Great post!", user_id=123)
        print(f"Успех: {comment1}")
        comment2 = Comment(text="Nice article.", guest_name="Anonymous Reader")
        print(f"Успех: {comment2}")
    except ValidationError as e:
        print(f"Ошибка: {e}")

    # Демонстрация ошибок
    try:
        Comment(text="Ambiguous comment.", user_id=456, guest_name="John Doe")
    except ValidationError as e:
        print(f"\nОшибка валидации: {e}")

    try:
        Comment(text="No author.")
    except ValidationError as e:
        print(f"\nОшибка валидации: {e}")
