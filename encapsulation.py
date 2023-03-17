class Mage:
    def __init__(self, health=60, mana=100):
        self.__health = health
        self.__mana = mana

    def get_health(self):
        return self.__health

    def set_health(self, poinst):
        self.__health += poinst
        if self.__health > 100:
            self.__health = 100
        elif self.__health < 0:
            self.__health = 0

    def introduces(self):
        print('---------------')
        print(f'Class. {self.__class__.__name__}',
              f'\nHealth: {self.__health}',
              f'\nStamina: {self.__mana}')
        print('---------------')

    def heals(self, target):
        print('--------------------------')
        if self.__mana < 20:
            print('Недостаточно магии для использования этой способности.')
        else:
            print('--------------------------')
            print(f'{self.__class__.__name__} применяет заклинание лечения',
                  f'к {target.__class__.__name__}')
            target.set_health(10)
            self.__mana -= 20
            print(f'Здоровье у {target.__class__.__name__} повыселось до {target.get_health}'
                  f'\nУ {self.__class__.__name__} осталось {self.__mana} магии')
        print('--------------------------')

    def attacks(self, target):
        print('--------------------------')
        if target.get_health() <= 3:
            print(f'{self.__class__.__name__} наносит последний удар и побеждает {target.__class__.__name__} '
                  f'\n{target.__class__.__name__} покидает отряд')
            target.set_health(-3)
        else:
            print(f'{self.__class__.__name__} применяет заклинание урона',
                  f'к {target.__class__.__name__}')
            target.set_health(-3)
            print(f'Здоровье у {target.__class__.__name__} упало до {target.get_health()}')
        print('--------------------------')


class Warrior:
    def __init__(self, health=100, stamina=100):
        self.__health = health
        self.__stamina = stamina

    def get_health(self):
        return self.__health

    def set_health(self, poinst):
        self.__health += poinst
        if self.__health > 100:
            self.__health = 100
        elif self.__health < 0:
            self.__health = 0

    def introduces(self):
        print('---------------')
        print(f'Class. {self.__class__.__name__}',
              f'\nHealth: {self.__health}',
              f'\nStamina: {self.__stamina}')
        print('---------------')

    def heals(self, target):
        print('--------------------------')
        if self.__stamina < 20:
            print('Недостаточно сил для использования этой способности.')
        else:
            print(f'{self.__class__.__name__} применяет траво лечение',
                  f'к {target.__class__.__name__}')
            target.set_health(+10)
            self.__stamina -= 20
            print(f'Здоровье у {target.__class__.__name__} повыселось до {target.get_health()}'
                  f'\nУ {self.__class__.__name__} осталось {self.__stamina} выносливость')
        print('--------------------------')

    def attacks(self, target):
        print('--------------------------')
        if target.get_health() <= 3:
            print(f'{self.__class__.__name__} наносит последний удар и побеждает {target.__class__.__name__} '
                  f'\n{target.__class__.__name__} покидает отряд')
            target.set_health(-3)
        else:
            print(f'{self.__class__.__name__} наносит урон мечём',
                  f'по {target.__class__.__name__}')
            target.set_health(-3)
            print(f'Здоровье у {target.__class__.__name__} упало до {target.get_health()}')
        print('--------------------------')


# unit1 = Warrior(100, 20)
# unit3 = Mage(97, 3)
# unit1.heals(unit3)
# unit1.heals(unit3)
