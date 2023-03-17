class Mage:
    def __init__(self, health=60, mana=100):
        self.__health = health
        self.mana = mana

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, new_health):
        if new_health > 100:
            self.__health = 100
        elif new_health < 0:
            self.__health = 0
        else:
            self.__health = new_health

    def introduces(self):
        print('---------------')
        print(f'Class. {self.__class__.__name__}',
              f'\nHealth: {self.health}',
              f'\nStamina: {self.mana}')
        print('---------------')

    def heals(self, target):
        print('--------------------------')
        print(f'{self.__class__.__name__} применяет заклинание лечения',
              f'к {target.__class__.__name__}')
        target.health += 10
        self.mana -= 20
        print(f'Здоровье у {target.__class__.__name__} повыселось до {target.health}'
              f'\nУ {self.__class__.__name__} осталось {self.mana} магии')
        print('--------------------------')

    def attacks(self, target):
        print('--------------------------')
        print(f'{self.__class__.__name__} применяет заклинание урона',
              f'к {target.__class__.__name__}')
        target.health -= 3
        print(f'Здоровье у {target.__class__.__name__} упало до {target.health}')
        print('--------------------------')


class Warrior:
    def __init__(self, health=100, stamina=100):
        self.__health = health
        self.__stamina = stamina

    @property
    def health(self):
        return self.__health

    @property
    def stamina(self):
        return self.__stamina

    @health.setter
    def health(self, new_health):
        if new_health > 100:
            self.__health = 100
        elif new_health < 0:
            self.__health = 0
        else:
            self.__health = new_health

    @stamina.setter
    def stamina(self, new_stamina):
        if new_stamina > 100:
            self.__stamina = 100
        elif new_stamina < 0:
            self.__stamina = 0
        else:
            self.__stamina = new_stamina

    def introduces(self):
        print('---------------')
        print(f'Class. {self.__class__.__name__}',
              f'\nHealth: {self.health}',
              f'\nStamina: {self.stamina}')
        print('---------------')

    def heals(self, target):
        print('--------------------------')
        print(f'{self.__class__.__name__} применяет траво лечение',
              f'к {target.__class__.__name__}')
        target.health += 10
        self.stamina -= 20
        print(f'Здоровье у {target.__class__.__name__} повыселось до {target.health}'
              f'\nУ {self.__class__.__name__} осталось {self.stamina} выносливость')
        print('--------------------------')

    def attacks(self, target):
        print('--------------------------')
        print(f'{self.__class__.__name__} наносит урон мечём',
              f'по {target.__class__.__name__}')
        target.health -= 3
        print(f'Здоровье у {target.__class__.__name__} упало до {target.health}')
        print('--------------------------')

# unit1 = Warrior()
# unit2 = Warrior()
unit3 = Mage()
# # unit4 = Mage(health=50, mana=110)
# # unit3.introduces()
# unit1.attacks(unit3)
# unit3.heals(unit1)
# unit1.heals(unit3)
# print(unit3.__dict__)
print(unit3.health)
