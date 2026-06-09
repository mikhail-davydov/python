class FieldTracker:
    fields = tuple()

    def __init__(self):
        self.fields_dict = {}

    def base(self, attr_name):
        if attr_name in self.fields_dict:
            return self.fields_dict[attr_name]
        return self.__dict__[attr_name]

    def has_changed(self, attr_name):
        return attr_name in self.fields_dict

    def changed(self):
        return self.fields_dict

    def save(self):
        self.fields_dict = {}

    def __setattr__(self, key, value):
        if hasattr(self, key) and key not in self.fields_dict:
            self.fields_dict[key] = getattr(self, key)
        self.__dict__[key] = value


# alt

class FieldTracker:
    def __init__(self):
        self._values = {
            field: getattr(self, field)
            for field in self.fields
        }

    def base(self, field):
        return self._values[field]

    def has_changed(self, field):
        return self._values[field] != getattr(self, field)

    def changed(self):
        return {
            field: self.base(field)
            for field in self.fields
            if self.has_changed(field)
        }

    def save(self):
        for field in self.fields:
            self._values[field] = getattr(self, field)
