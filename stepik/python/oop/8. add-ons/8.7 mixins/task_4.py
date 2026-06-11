class ToStringMixin:
    def __repr__(self):
        dict_list = [f'{key!r}: {value!r}' for key, value in self.__dict__.items()]
        if len(dict_list) > 6:
            return f'{self.__class__.__name__}({{{', '.join(dict_list[:6])}, ...}})'
        else:
            return f'{self.__class__.__name__}({{{', '.join(dict_list)}}})'


# alt

class ToStringMixin:
    def __repr__(self):
        if len(self.__dict__) <= 6:
            return f'{self.__class__.__name__}({self.__dict__})'
        items, attrs = iter(self.__dict__.items()), []
        for _ in range(6):
            key, value = next(items)
            attrs.append(f'{key!r}: {value!r}, ')
        return f'{self.__class__.__name__}({{{"".join(attrs)}...}})'
