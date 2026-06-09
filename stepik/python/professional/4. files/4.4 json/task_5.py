import json


def is_correct_json(string: str) -> bool:
    try:
        json.loads(string)
        return True
    except json.JSONDecodeError:
        return False


print(is_correct_json('number = 17'))