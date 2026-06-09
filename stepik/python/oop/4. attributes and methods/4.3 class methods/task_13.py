class Postman:
    def __init__(self):
        self.delivery_data = []

    def add_delivery(self, street, house, apart):
        self.delivery_data.append((street, house, apart))

    def get_houses_for_street(self, street):
        return list(
            {house: None
             for street_, house, _ in self.delivery_data
             if street_ == street}
        )

    def get_flats_for_house(self, street, house):
        return list(
            {flat: None
             for street_, house_, flat in self.delivery_data
             if street_ == street and house_ == house}
        )


postman = Postman()

print(postman.delivery_data)
print(postman.get_houses_for_street('3-я ул. Строителей'))
print(postman.get_flats_for_house('3-я ул. Строителей', 25))

print('-' * 10)

postman = Postman()

postman.add_delivery('Советская', 151, 74)
postman.add_delivery('Советская', 151, 75)
postman.add_delivery('Советская', 90, 2)
postman.add_delivery('Советская', 151, 74)

print(postman.get_houses_for_street('Советская'))
print(postman.get_flats_for_house('Советская', 151))
