from itertools import cycle


class Gun:
    def __init__(self):
        self.sounds = cycle(('pif', 'paf'))
        self.count = 0

    def shoot(self):
        print(next(self.sounds))
        self.count += 1

    def shots_count(self):
        return self.count

    def shots_reset(self):
        self.count = 0
        self.sounds = cycle(('pif', 'paf'))


# alt
class Gun:
    def __init__(self):
        self.shots = 0

    def shoot(self):
        if self.shots % 2:
            print('paf')
        else:
            print('pif')
        self.shots += 1

    def shots_count(self):
        return self.shots

    def shots_reset(self):
        self.shots = 0


gun = Gun()

gun.shoot()
gun.shoot()
print(gun.shots_count())
gun.shots_reset()
print(gun.shots_count())
gun.shoot()
print(gun.shots_count())
