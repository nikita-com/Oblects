from game_objects.Game_classes import Warrior, Mage
import random


class Archer(Warrior):
    def __init__(self, health=100, stamina=100, arrows=20):
        super().__init__(health, stamina)
        self.arrows = arrows

    def attacks(self, target):
        # a = random.randint(1, 100)
        # if a < 30:
        #     self.attacks(target)
        # else:
        print('--------------------------')
        print(f'{self.__class__.__name__} стреляет из лука',
              f'по {target.__class__.__name__}')
        target.health -= 4
        self.arrows -= 1
        print(f'Здоровье у {target.__class__.__name__} упало до {target.health}'
              f'\nУ {self.__class__.__name__} осталось {self.arrows} стрел')
        print('--------------------------')

    def introduces(self):
        super().introduces()
        print(f'Arrows {self.arrows}')
        print('---------------')

    def sniper_shot(self, target):
        if self.stamina >= 30:
            print('--------------------------')
            print(f'{self.__class__.__name__} прицеливается и стреляет из лука',
                  f'по {target.__class__.__name__}')
            target.health -= 15
            self.arrows -= 1
            self.stamina -= 30
            print(f'Здоровье у {target.__class__.__name__} упало до {target.health}'
                  f'\nУ {self.__class__.__name__} осталось {self.arrows} стрел'
                  f' и {self.stamina} выносливости')
            print('--------------------------')
        else:
            print('--------------------------')
            print(f'у {self.__class__.__name__} недостаточно выносливости')
            print('--------------------------')


class Alchemist(Mage):
    def __init__(self, health=100, mana=100, flasks=10):
        super().__init__(health, mana)
        self.flasks = flasks

    def introduces(self):
        super().introduces()
        print(f'Arrows {self.flasks}')
        print('---------------')

    def attacks(self, target):
        print('--------------------------')
        print(f'{self.__class__.__name__} кинул банку с огурцами',
              f'в {target.__class__.__name__}')
        target.health -= 10
        self.health -= 3
        self.flasks -= 1
        print(f'Здоровье у {target.__class__.__name__} упало до {target.health}'
              f', Здоровье у {self.__class__.__name__} упало до {self.health}'
              f'\nУ {self.__class__.__name__} осталось {self.flasks} банок с огурцами')
        print('--------------------------')

anton = Alchemist()
genadij = Archer()
anton.heals(anton)
genadij.heals(anton)
genadij.sniper_shot(anton)
