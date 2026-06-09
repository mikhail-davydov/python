class Pet:
    pets = []

    def __init__(self, name):
        self.name = name
        self.pets.append(self)

    @classmethod
    def first_pet(cls):
        return cls.pets[0] if cls.pets else None

    @classmethod
    def last_pet(cls):
        return cls.pets[-1] if cls.pets else None

    @classmethod
    def num_of_pets(cls):
        return len(cls.pets)


print(Pet.first_pet())
print(Pet.last_pet())
print(Pet.num_of_pets())

print(10 * '-')

pet1 = Pet('Ratchet')
pet2 = Pet('Clank')
pet3 = Pet('Rivet')

print(Pet.first_pet().name)
print(Pet.last_pet().name)
print(Pet.num_of_pets())
