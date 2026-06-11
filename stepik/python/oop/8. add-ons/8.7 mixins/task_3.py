class AttributesMixin:
    def get_public_attributes(self):
        return [
            (key, value)
            for key, value
            in self.__dict__.items()
            if not str.startswith(key, '_')
        ]

    def get_protected_attributes(self):
        return [
            (key, value)
            for key, value
            in self.__dict__.items()
            if str.startswith(key, '_') and str.find(key, '__') == -1
        ]

    # alt
    def get_protected_attributes(self):
        attrs = []
        cls = self.__class__.__name__
        for attr, value in self.__dict__.items():
            if attr.startswith('_') and not attr.startswith(f'_{cls}__'):
                attrs.append((attr, value))
        return attrs
