from game_objects.encapsulation import Warrior, Mage
import random


class Knigth(Warrior):
    def __init__(self, health=100, armor=100, stamina=100):
        super().__init__(health, stamina)
        self.__armor = armor

    def set_health(self, points):
        if points > 0:
            super().set_health(points)
        else:
            if self.__armor > abs(points):
                self.__armor += points
                print(f'броня уменьшена до {self.__armor}')
            elif self.__armor == abs(points):
                self.__armor = 0
                print(f'у {self.__class__.__name__} унечтожина броня')
            else:
                points = points + self.__armor
                self.__armor = 0
                super().set_health(points)
                print(f'у {self.__class__.__name__} унечтожина броня')

    def __criticai_hit(self, target):
        print('--------------------------')
        if target.get_health() <= 10:
            print(f'{self.__class__.__name__} наносит последний критический удар и побеждает {target.__class__.__name__}'
                  f'\n{target.__class__.__name__} покидает отряд')
            target.set_health(-10)
        else:
            print(f'{self.__class__.__name__} наносит критический урон мечём',
                  f'по {target.__class__.__name__}')
            target.set_health(-10)
            print(f'Здоровье у {target.__class__.__name__} упало до {target.get_health()}')
            print('--------------------------')

    def attacks(self, target):
        a = random.randint(1, 100)
        if a < 40:
            self.__criticai_hit(target)
        else:
            super().attacks(target)


class Wizard(Mage):
    def __init__(self, health=100, barrier=100, stamina=100):
        super().__init__(health, stamina)
        self.__barrier = barrier

    def set_health(self, points):
        if points > 0:
            super().set_health(points)
        else:
            if self.__barrier > abs(points):
                self.__barrier += points
                print(f'барьер уменьшена до {self.__barrier}')
            elif self.__barrier == abs(points):
                self.__barrier = 0
                print(f'у {self.__class__.__name__} унечтожина барьер')
            else:
                points = points + self.__barrier
                self.__barrier = 0
                super().set_health(points)
                print(f'у {self.__class__.__name__} унечтожина барьер')

    def __fireball(self, target):
        print('--------------------------')
        if target.get_health() <= 15:
            print(f'{self.__class__.__name__} вызывает фаербол и побеждает {target.__class__.__name__}'
                  f'\n{target.__class__.__name__} покидает отряд')
            target.set_health(-15)
        else:
            print(f'{self.__class__.__name__} вызывает фаербол',
                  f'по {target.__class__.__name__}')
            target.set_health(-15)
            print(f'Здоровье у {target.__class__.__name__} упало до {target.get_health()}')
            print('--------------------------')

    def attacks(self, target):
        a = random.randint(1, 100)
        if a < 20:
            self.__fireball(target)
        else:
            super().attacks(target)


unit2 = Wizard()
unit1 = Knigth(90, 90, 90)
unit2.attacks(unit1)
print(unit2.__dict__)
