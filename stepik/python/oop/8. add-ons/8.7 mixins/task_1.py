import json


class JsonSerializableMixin:
    def to_json(self):
        return json.dumps(self.__dict__)
