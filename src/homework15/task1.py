'''
Создайте  модель из жизни. Это может быть бронирование комнаты в отеле, покупка билета в
транспортной компании, или простая РПГ. Создайте несколько объектов классов, которые описывают
ситуацию. Объекты должны содержать как атрибуты так и методы класса для симуляции различных
действий. Программа должна инстанцировать объекты и эмулировать какую-либо ситуацию -
вызывать методы, взаимодействие объектов и т.д.
'''


class Heroes:

    def __init__(self, name, race='incognito'):
        self.name = name
        self.race = race
        self.show_bio()

    def show_bio(self):
        '''Show biography of hero'''
        print('You created Hero ' + self.name + ' and his race is ' + self.race)

    def run(self):
        '''Hero can run'''
        print(self.name + ' runing')

    def fire(self):
        '''Hero can fire'''
        print(self.name + ' firing')


class Weapon:

    def __init__(self):
        self.righ_hand = None
        self.left_hand = None

    def show_right_weapon(self):
        print('right hand has weapon ' + self.righ_hand)

    def show_left_weapon(self):
        print('left hand has weapon ' + self.left_hand)

    def show_all_weapon(self):
        print('right weapon is ' + self.righ_hand + ', left weapon is ' + self.left_hand)

    def set_right_weapon(self, type_weapon):
        self.righ_hand = type_weapon

    def set_left_weapon(self, type_weapon):
        self.left_hand = type_weapon


class Transformer(Heroes):

    def __init__(self, name, race, right_hand, left_hand):
        Heroes.__init__(self, name, race)
        self.weapon = Weapon()
        self.weapon.set_right_weapon(right_hand)
        self.weapon.set_left_weapon(left_hand)

    def show_all_weapon(self):
        self.weapon.show_all_weapon()

    def show_right_weapon(self):
        self.weapon.show_right_weapon()

    def show_left_weapon(self):
        self.weapon.show_left_weapon()

    def transform_to_car(self):
        '''Hero to transform to car'''
        print('transform to car')


class Ork(Heroes):

    def __init__(self, name, race, right_hand, left_hand):
        Heroes.__init__(self, name, race)
        self.weapon = Weapon()
        self.weapon.set_right_weapon(right_hand)
        self.weapon.set_left_weapon(left_hand)

    def show_all_weapon(self):
        self.weapon.show_all_weapon()

    def show_right_weapon(self):
        self.weapon.show_right_weapon()

    def show_left_weapon(self):
        self.weapon.show_left_weapon()

    def mode_berserk(self):
        '''Hero  to mode berserk'''
        print('turned on mode of Berserk')


class Elf(Heroes):

    def __init__(self, name, race, right_hand, left_hand):
        Heroes.__init__(self, name, race)
        self.weapon = Weapon()
        self.weapon.set_right_weapon(right_hand)
        self.weapon.set_left_weapon(left_hand)

    def show_all_weapon(self):
        self.weapon.show_all_weapon()

    def show_right_weapon(self):
        self.weapon.show_right_weapon()

    def show_left_weapon(self):
        self.weapon.show_left_weapon()

    def became_invisible(self):
        '''Hero bacame the invisble'''
        print('bacame the invisble')


class Human(Heroes):

    def __init__(self, name, race, right_hand, left_hand):
        Heroes.__init__(self, name, race)
        self.weapon = Weapon()
        self.weapon.set_right_weapon(right_hand)
        self.weapon.set_left_weapon(left_hand)

    def show_all_weapon(self):
        self.weapon.show_all_weapon()

    def show_right_weapon(self):
        self.weapon.show_right_weapon()

    def show_left_weapon(self):
        self.weapon.show_left_weapon()

    def invoke_golem(self):
        '''Hero invoked golem'''
        print('invoked golem')


class Rpg:

    def create_transformer(self):
        '''Create transformer'''
        transformer = Transformer('Optimus', 'Transformer', 'Plasma', 'Rocket')
        transformer.show_all_weapon()
        transformer.transform_to_car()
        transformer.run()
        transformer.fire()

    def create_ork(self):
        '''Create ork'''
        ork = Ork('Tamar', 'Ork', 'Ax', 'Shield')
        ork.show_right_weapon()
        ork.mode_berserk()
        ork.run()
        ork.fire()

    def create_elf(self):
        '''Create elf'''
        elf = Elf('Driad', 'Elf', 'Bow and arrows', 'Knife')
        elf.became_invisible()
        elf.show_left_weapon()
        elf.run()
        elf.fire()

    def create_human(self):
        '''Create human'''
        human = Human('Valera', 'Human', 'cudgel', 'spear')
        human.show_all_weapon()
        human.invoke_golem()
        human.run()
        human.fire()

    def run_game(self):
        '''Run_game'''
        self.create_transformer()
        self.create_ork()
        self.create_elf()
        self.create_human()


Rpg().run_game()
