class UpperPrintString(str):
    def __str__(self):
        return super().__str__().upper()
