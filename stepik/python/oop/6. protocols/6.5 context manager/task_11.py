class HtmlTag:
    counter = -1

    def __init__(self, tag, inline: bool = False):
        self.tag = tag
        self.inline = inline
        self.indent = '  '

    def print(self, text):
        prefix = (__class__.counter + 1) * self.indent
        text = f'{text}' \
            if self.inline \
            else f'{prefix}{text}\n'
        print(text, end='')

    def __enter__(self):
        __class__.counter += 1
        prefix = __class__.counter * self.indent
        text = f'{prefix}<{self.tag}>' \
            if self.inline \
            else f'{prefix}<{self.tag}>\n'
        print(text, end='')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        prefix = __class__.counter * self.indent
        text = f'</{self.tag}>' \
            if self.inline \
            else f'{prefix}</{self.tag}>'
        print(text)
        __class__.counter -= 1
        return False


# alt

class HtmlTag:
    _level = 0

    def __init__(self, tag, inline=False):
        self.tag = tag
        self.inline = inline
        self._end = '' if self.inline else '\n'

    def __enter__(self):
        print(self._current_indent + f'<{self.tag}>', end=self._end)
        type(self)._level += 1
        return self

    def __exit__(self, *exc_info):
        type(self)._level -= 1
        print(self._indent + f'</{self.tag}>')

    def print(self, message):
        print(self._indent + message, end=self._end)

    @property
    def _indent(self):
        return '' if self.inline else self._current_indent

    @property
    def _current_indent(self):
        return '  ' * type(self)._level
