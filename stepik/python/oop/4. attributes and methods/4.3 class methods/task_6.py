class Gun:
    def __init__(self):
        self.is_pif = True

    def shoot(self):
        shoot_sound = 'pif' if self.is_pif else 'paf'
        print(shoot_sound)
        self.is_pif = not self.is_pif


# alt
class Gun:
    def __init__(self):
        self.sounds = cycle(('pif', 'paf'))

    def shoot(self):
        print(next(self.sounds))


gun = Gun()

gun.shoot()
gun.shoot()
gun.shoot()
gun.shoot()
