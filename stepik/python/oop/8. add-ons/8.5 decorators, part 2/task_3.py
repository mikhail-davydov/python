import json


def jsonattr(filename: str):
    def wrapper(cls):
        with open(filename, encoding='u8') as i_file:
            attr_dict = json.load(i_file)
            for key, value in attr_dict.items():
                setattr(cls, key, value)
        return cls

    return wrapper


# alt

class jsonattr:
    def __init__(self, filename):
        self.filename = filename

    def __call__(self, cls):
        with open(self.filename, 'r') as file:
            json_data = json.load(file)
            for key, value in json_data.items():
                setattr(cls, key, value)
        return cls
