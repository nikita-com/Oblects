class Warrior:
    def __init__(self, health=100, stamina=100):
        self.health = health
        self.stamina = stamina

    def __setattr__(self, attribute, value):
        if value > 100:
            self.__dict__[attribute] = 100
        elif value < 0:
            self.__dict__[attribute] = 0
        else:
            self.__dict__[attribute] = value


    def __call__(self):
        print('---------------')
        print(f'Class: {self.__class__.__name__}',
              f'\nHealth: {self.health}',
              f'\nStamina: {self.stamina}')
        print('---------------')

    def __add__(self, target):
        if isinstance(target, (Mage, Warrior)):
            print('---------------')
            print(f'{self.__class__.__name__} накладывает повязку из',
                  f'целебных трав {target.__class__.__name__}')
            self.stamina -= 20
            target.health += 10
            print(f'Здоровье у {target.__class__.__name__} повышено до {target.health}',
                  f'\nУ {self.__class__.__name__} осталось {self.stamina} единиц запаса сил')
            print('---------------')
        elif isinstance(target, int):
            print('---------------')
            print(f'{self.__class__.__name__} получил {target} единиц здоровья')
            print('---------------')
        elif isinstance(target, list):
            target.append(self)
            print('---------------')
            print(f'{self.__class__.__name__} добавлен в список {target[0]}')
            print('---------------')

    def __sub__(self, target):
        if isinstance(target, (Mage, Warrior)):
            print('---------------')
            print(f'{self.__class__.__name__} наносит урон мечом {target.__class__.__name__}')
            target.health -= 3
            print(f'Здоровье у {target.__class__.__name__} понижено до {target.health}')
            print('---------------')
        elif isinstance(target, int):
            self.health -= target
            print('---------------')
            print(f'{self.__class__.__name__} получил урон в {target} единиц здоровья')
            print('---------------')
        elif isinstance(target, list):
            target.remove(self)
            print('---------------')
            print(f'{self.__class__.__name__} исключён из списока {target[0]}')
            print('---------------')


class Mage:
    def __init__(self, health=60, mana=120):
        self.health = health
        self.mana = mana

    def __setattr__(self, attribute, value):
        if attribute == 'health':
            if value > 60:
                self.__dict__[attribute] = 60
            elif value < 0:
                self.__dict__[attribute] = 0
            else:
                self.__dict__[attribute] = value
        elif attribute == 'mana':
            if value > 120:
                self.__dict__[attribute] = 60
            elif value < 0:
                self.__dict__[attribute] = 0
            else:
                self.__dict__[attribute] = value

    def __str__(self):
        s1 = '---------------\n'
        s2 = f'Class: {self.__class__.__name__}\n'
        s3 = f'Health: {self.health}\n'
        s4 = f'Mana: {self.mana}\n'
        s5 = '---------------\n'
        return s1 + s2 + s3 + s4 + s5

    def __add__(self, target):
        if isinstance(target, (Mage, Warrior)):
            print('---------------')
            print(f'{self.__class__.__name__} применяет заклинание лечения',
                  f'к {target.__class__.__name__}')
            target.health += 10
            self.mana -= 20
            print(f'Здоровье у {target.__class__.__name__} повышено до {target.health}',
                  f'\nУ {self.__class__.__name__} осталось {self.mana} единиц магии')
            print('---------------')
        elif isinstance(target, int):
            self.health += target
            print('---------------')
            print(f'{self.__class__.__name__} получил {target} единиц здоровья')
            print('---------------')
        elif isinstance(target, list):
            target.append(self)
            print('---------------')
            print(f'{self.__class__.__name__} добавлен в список {target[0]}')
            print('---------------')

    def __sub__(self, target):
        if isinstance(target, (Mage, Warrior)):
            print(f'{self.__class__.__name__} наносит урон магией {target.__class__.__name__}')
            target.health -= 3
            print(f'Здоровье у {target.__class__.__name__} понижено до {target.health}')
            print('---------------')
        elif isinstance(target, int):
            self.health -= target
            print('---------------')
            print(f'{self.__class__.__name__} получил урон в {target} единиц здоровья')
            print('---------------')
        elif isinstance(target, list):
            target.remove(self)
            print('---------------')
            print(f'{self.__class__.__name__} исключён из списока {target[0]}')
            print('---------------')


squad = ['squad']
unit1 = Warrior()
unit2 = Mage()
# unit1 + squad
# unit1 - squad
# unit1 - unit2
# unit1 - 5
unit1.health = 103
unit2.mana = -2
