'''
Создайте  модель из жизни. Это может быть бронирование комнаты в отеле, покупка билета в
транспортной компании, или простая РПГ. Создайте несколько объектов классов, которые описывают
ситуацию. Объекты должны содержать как атрибуты так и методы класса для симуляции различных
действий. Программа должна инстанцировать объекты и эмулировать какую-либо ситуацию -
вызывать методы, взаимодействие объектов и т.д.
'''


class Heroes:

    def __init__(self, name, race):
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

    def __init__(self, righ_hand, left_hand):
        self.righ_hand = righ_hand
        self.left_hand = left_hand

    def show_weapon(self, is_right_hand):
        '''Hero show weapon'''
        if is_right_hand is True:
            print('right hand has weapon ' + self.righ_hand)
        elif is_right_hand is False:
            print('left hand has weapon ' + self.left_hand)
        else:
            print('right weapon is ' + self.righ_hand + ', left weapon is ' + self.left_hand)


class Transformer(Heroes, Weapon):

    def __init__(self, name, race, right_hand, left_hand):
        Heroes.__init__(self, name, race)
        Weapon.__init__(self, right_hand, left_hand)

    def transform_to_car(self):
        '''Hero to transform to car'''
        print('transform to car')


class Ork(Heroes, Weapon):

    def __init__(self, name, race, right_hand, left_hand):
        Heroes.__init__(self, name, race)
        Weapon.__init__(self, right_hand, left_hand)

    def mode_berserk(self):
        '''Hero  to mode berserk'''
        print('turned on mode of Berserk')


class Elf(Heroes, Weapon):

    def __init__(self, name, race, right_hand, left_hand):
        Heroes.__init__(self, name, race)
        Weapon.__init__(self, right_hand, left_hand)

    def became_invisible(self):
        '''Hero bacame the invisble'''
        print('bacame the invisble')


class Human(Heroes, Weapon):

    def __init__(self, name, race, right_hand, left_hand):
        Heroes.__init__(self, name, race)
        Weapon.__init__(self, right_hand, left_hand)

    def invoke_golem(self):
        '''Hero invoked golem'''
        print('invoked golem')


class Rpg:

    def create_transformer(self):
        '''Create transformer'''
        transformer = Transformer('Optimus', 'Transformer', 'Plasma', 'Rocket')
        transformer.show_weapon(None)
        transformer.transform_to_car()
        transformer.run()
        transformer.fire()

    def create_ork(self):
        '''Create ork'''
        ork = Ork('Tamar', 'Ork', 'Ax', 'Shield')
        ork.show_weapon(True)
        ork.mode_berserk()
        ork.run()
        ork.fire()

    def create_elf(self):
        '''Create elf'''
        elf = Elf('Driad', 'Elf', 'Bow and arrows', 'Knife')
        elf.became_invisible()
        elf.show_weapon(False)
        elf.run()
        elf.fire()

    def create_human(self):
        '''Create human'''
        human = Human('Valera', 'Human', 'cudgel', 'spear')
        human.show_weapon(None)
        human.invoke_golem()
        human.run()
        human.fire()

    def run_game(self):
        '''Run_game'''
        self.create_transformer()
        self.create_elf()
        self.create_ork()
        self.create_human()


Rpg().run_game()
