def is_safe_request(messages: list) -> bool:
    # Проверка: есть ли хотя бы одно сообщение с role == "system"
    has_system_message = any(
        isinstance(msg, dict) and msg.get("role") == "system"
        for msg in messages
    )

    # Проверка: каждое сообщение содержит ключи "role" и "content"
    all_messages_valid = all(
        isinstance(msg, dict) and "role" in msg and "content" in msg
        for msg in messages
    )

    return has_system_message and all_messages_valid


#

def truncate_prompt(text: str, max_length: int) -> str:
    # Если длина текста меньше или равна max_length, возвращаем текст без изменений
    if len(text) <= max_length:
        return text

    # Находим самую правую позицию пробела в пределах первых max_length символов
    substring = text[:max_length]
    last_space = substring.rfind(' ')

    if last_space == -1:
        # Пробел не найден (например, одно длинное слово)
        return "..."
    else:
        # Обрезаем текст до пробела и добавляем "..."
        return text[:last_space] + "..."


#

class LLMFactory:
    @staticmethod
    def create(provider: str):
        if provider == "openai":
            return OpenAIClient()
        if provider == "ollama":
            return OllamaClient()
        raise ValueError


class OpenAIClient:
    def generate(self, messages):
        return "mocked response"


class OllamaClient:
    def generate(self, messages):
        return "mocked response"


#

# from mistralai import Mistral

system_prompt = "Ты — генератор JSON. Ответ должен быть строго валидным JSON с полями: 'term' (строка) и 'definition' (строка до 100 символов)."
user_prompt = "Определи термин: FastAPI"

client = Mistral(api_key="test_key")

response = client.chat.complete(
    model="mistral-small-latest",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ],
    temperature=0.0,
    max_tokens=120
)

print(response.choices[0].message.content)
