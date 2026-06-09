class Color:

    def __init__(self, hexcode):
        self.hexcode = hexcode

    @property
    def hexcode(self):
        return self.__hexcode

    @hexcode.setter
    def hexcode(self, hexcode):
        self.__hexcode = hexcode
        self.r, self.g, self.b = self.__hexcode_to_rgb(hexcode)

    def __hexcode_to_rgb(self, hexcode):
        return int(hexcode[:2], base=16), int(hexcode[2:4], base=16), int(hexcode[4:], base=16)


color = Color('0000FF')

print(color.hexcode)
print(color.r)
print(color.g)
print(color.b)

print(10 * '-')

color = Color('0000FF')

color.hexcode = 'A782E3'
print(color.hexcode)
print(color.r)
print(color.g)
print(color.b)
