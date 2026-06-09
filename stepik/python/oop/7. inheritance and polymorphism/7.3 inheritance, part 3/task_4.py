class TitledText(str):
    def __new__(cls, content, text_title):
        result = super().__new__(cls, content)
        result.text_title = text_title
        return result

    def title(self):
        return self.text_title