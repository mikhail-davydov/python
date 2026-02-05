import json


def load_json(file_path: str) -> dict:
    """Загрузка данных из JSON-файла."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        raise ValueError(f'Файл "{file_path}" не найден.')
    except json.JSONDecodeError:
        raise ValueError('Ошибка формата JSON файла.')
