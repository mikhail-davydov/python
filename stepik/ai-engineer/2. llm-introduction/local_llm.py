import requests

response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "mistral",
        "prompt": "Что такое Alembic?",
        "stream": False,
        "options": {
            "temperature": 0.2,
            "num_ctx": 2048,
        }
    }
)

print(response.json()["response"])


import ollama

response = ollama.chat(
    model='mistral',
    messages=[{'role': 'user', 'content': 'Что такое Alembic?'}],
    options={'temperature': 0.2, 'num_ctx': 2048}
)
print(response['message']['content'])


def prompt_to_chat_messages(prompt: str) -> list:
    return [{'role': 'user', 'content': prompt}]


def build_generate_request(model: str, prompt: str) -> dict:
    return {
        'model': model,
        'prompt': prompt,
    }


def build_chat_request(model: str, messages: list, temperature: float) -> dict:
    return {
        'model': model,
        'messages': messages,
        'stream': False,
        'options': {
            'temperature': temperature,
        },
    }


def ensure_system_prompt(messages: list, default_system: str) -> list:
    # Проверка: есть ли хотя бы одно сообщение с role == "system"
    has_system_message = any(
        isinstance(msg, dict) and msg.get("role") == "system"
        for msg in messages
    )

    if has_system_message:
        return messages

    messages.insert(0, {'role': 'system', 'content': default_system})
    return messages
