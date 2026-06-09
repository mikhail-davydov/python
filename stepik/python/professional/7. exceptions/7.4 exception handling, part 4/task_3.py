import json


def deserialize_json(json_filename: str) -> object:
    try:
        with open(json_filename, encoding='u8') as i_file:
            return json.load(i_file)
    except FileNotFoundError:
        return 'Файл не найден'
    except ValueError:
        return 'Ошибка при десериализации'


print(deserialize_json(input()))
