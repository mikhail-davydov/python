class Item:
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price

    def __str__(self):
        return f'{self.name}, {self.price}$'


class ShoppingCart:
    def __init__(self, items: list[Item] = ()):
        self.items = list(items)

    def add(self, item: Item):
        self.items.append(item)

    def total(self):
        return sum(item.price for item in self.items)

    def remove(self, name: str):
        self.items = list(filter(lambda item: item.name != name, self.items))

    def __str__(self):
        return '\n'.join(str(item) for item in self.items)
