import io
import sys
import task1
import unittest


class TestHeroes(unittest.TestCase):
    captured_output = None

    def setUp(self):
        self.heroes = task1.Heroes('Optimus', 'Transformer')
        self.captured_output = io.StringIO()
        sys.stdout = self.captured_output

    def tearDown(self):
        self.captured_output = None

    def test_init(self):
        self.assertEqual(self.heroes.name, 'Optimus')
        self.assertEqual(self.heroes.race, 'Transformer')

    def test_show_bio(self):
        expected = 'You created Hero Optimus and his race is Transformer\n'
        self.heroes.show_bio()
        sys.stdout = sys.__stdout__
        self.assertEqual(expected, self.captured_output.getvalue())

    def test_run(self):
        expected = 'Optimus runing\n'
        self.heroes.run()
        sys.stdout = sys.__stdout__
        self.assertEqual(expected, self.captured_output.getvalue())

    def test_fire(self):
        expected = 'Optimus firing\n'
        self.heroes.fire()
        sys.stdout = sys.__stdout__
        self.assertEqual(expected, self.captured_output.getvalue())


class TestWeapon(unittest.TestCase):
    captured_output = None

    def setUp(self):
        self.weapon = task1.Weapon()
        self.weapon.set_right_weapon('Plasma')
        self.weapon.set_left_weapon('Gun')
        self.captured_output = io.StringIO()
        sys.stdout = self.captured_output

    def tearDown(self):
        self.captured_output = None

    def test_set_right_weapon(self):
        expected = 'weapon one'
        self.weapon.set_right_weapon(expected)
        self.assertEqual(self.weapon.righ_hand, expected)

    def test_set_left_weapon(self):
        expected = 'weapon two'
        self.weapon.set_left_weapon(expected)
        self.assertEqual(self.weapon.left_hand, expected)

    def test_show_right_weapon(self):
        expected = 'right hand has weapon Plasma\n'
        self.weapon.show_right_weapon()
        sys.stdout = sys.__stdout__
        self.assertEqual(expected, self.captured_output.getvalue())

    def test_show_left_weapon(self):
        expected = 'left hand has weapon Gun\n'
        self.weapon.show_left_weapon()
        sys.stdout = sys.__stdout__
        self.assertEqual(expected, self.captured_output.getvalue())

    def test_show_all_weapon(self):
        expected = 'right weapon is Plasma, left weapon is Gun\n'
        self.weapon.show_all_weapon()
        sys.stdout = sys.__stdout__
        self.assertEqual(expected, self.captured_output.getvalue())


class TestTransformer(unittest.TestCase):
    captured_output = None

    def setUp(self):
        self.transformer = task1.Transformer('Optimus', 'Transformer', 'Plasma', 'Rocket')
        self.captured_output = io.StringIO()
        sys.stdout = self.captured_output

    def tearDown(self):
        self.captured_output = None

    def test_init(self):
        self.assertEqual(self.transformer.name, 'Optimus')
        self.assertEqual(self.transformer.race, 'Transformer')
        self.assertEqual(self.transformer.weapon.righ_hand, 'Plasma')
        self.assertEqual(self.transformer.weapon.left_hand, 'Rocket')

    def test_show_all_weapon(self):
        expected = 'right weapon is Plasma, left weapon is Rocket\n'
        self.transformer.show_all_weapon()
        sys.stdout = sys.__stdout__
        self.assertEqual(expected, self.captured_output.getvalue())

    def test_show_right_weapon(self):
        expected = 'right hand has weapon Plasma\n'
        self.transformer.show_right_weapon()
        sys.stdout = sys.__stdout__
        self.assertEqual(expected, self.captured_output.getvalue())

    def test_show_left_weapon(self):
        expected = 'left hand has weapon Rocket\n'
        self.transformer.show_left_weapon()
        sys.stdout = sys.__stdout__
        self.assertEqual(expected, self.captured_output.getvalue())

    def test_transform_to_car(self):
        expected = 'transform to car\n'
        self.transformer.transform_to_car()
        sys.stdout = sys.__stdout__
        self.assertEqual(expected, self.captured_output.getvalue())


class TestOrk(unittest.TestCase):
    captured_output = None

    def setUp(self):
        self.ork = task1.Ork('name_Ork', 'Ork', 'Axe', 'Shield')
        self.captured_output = io.StringIO()
        sys.stdout = self.captured_output

    def tearDown(self):
        self.captured_output = None

    def test_init(self):
        self.assertEqual(self.ork.name, 'name_Ork')
        self.assertEqual(self.ork.race, 'Ork')
        self.assertEqual(self.ork.weapon.righ_hand, 'Axe')
        self.assertEqual(self.ork.weapon.left_hand, 'Shield')

    def test_show_all_weapon(self):
        expected = 'right weapon is Axe, left weapon is Shield\n'
        self.ork.show_all_weapon()
        sys.stdout = sys.__stdout__
        self.assertEqual(expected, self.captured_output.getvalue())

    def test_show_right_weapon(self):
        expected = 'right hand has weapon Axe\n'
        self.ork.show_right_weapon()
        sys.stdout = sys.__stdout__
        self.assertEqual(expected, self.captured_output.getvalue())

    def test_show_left_weapon(self):
        expected = 'left hand has weapon Shield\n'
        self.ork.show_left_weapon()
        sys.stdout = sys.__stdout__
        self.assertEqual(expected, self.captured_output.getvalue())

    def test_mode_berserk(self):
        expected = 'turned on mode of Berserk\n'
        self.ork.mode_berserk()
        sys.stdout = sys.__stdout__
        self.assertEqual(expected, self.captured_output.getvalue())


class TestElf(unittest.TestCase):
    captured_output = None

    def setUp(self):
        self.elf = task1.Elf('name_Elf', 'Elf', 'Arc', 'Arrow')
        self.captured_output = io.StringIO()
        sys.stdout = self.captured_output

    def tearDown(self):
        self.captured_output = None

    def test_init(self):
        self.assertEqual(self.elf.name, 'name_Elf')
        self.assertEqual(self.elf.race, 'Elf')
        self.assertEqual(self.elf.weapon.righ_hand, 'Arc')
        self.assertEqual(self.elf.weapon.left_hand, 'Arrow')

    def test_show_all_weapon(self):
        expected = 'right weapon is Arc, left weapon is Arrow\n'
        self.elf.show_all_weapon()
        sys.stdout = sys.__stdout__
        self.assertEqual(expected, self.captured_output.getvalue())

    def test_show_right_weapon(self):
        expected = 'right hand has weapon Arc\n'
        self.elf.show_right_weapon()
        sys.stdout = sys.__stdout__
        self.assertEqual(expected, self.captured_output.getvalue())

    def test_show_left_weapon(self):
        expected = 'left hand has weapon Arrow\n'
        self.elf.show_left_weapon()
        sys.stdout = sys.__stdout__
        self.assertEqual(expected, self.captured_output.getvalue())

    def test_became_invisible(self):
        expected = 'bacame the invisble\n'
        self.elf.became_invisible()
        sys.stdout = sys.__stdout__
        self.assertEqual(expected, self.captured_output.getvalue())


class TestHuman(unittest.TestCase):
    captured_output = None

    def setUp(self):
        self.human = task1.Human('name_Man', 'Human', 'Sword', 'Gun')
        self.captured_output = io.StringIO()
        sys.stdout = self.captured_output

    def tearDown(self):
        self.captured_output = None

    def test_init(self):
        self.assertEqual(self.human.name, 'name_Man')
        self.assertEqual(self.human.race, 'Human')
        self.assertEqual(self.human.weapon.righ_hand, 'Sword')
        self.assertEqual(self.human.weapon.left_hand, 'Gun')

    def test_show_all_weapon(self):
        expected = 'right weapon is Sword, left weapon is Gun\n'
        self.human.show_all_weapon()
        sys.stdout = sys.__stdout__
        self.assertEqual(expected, self.captured_output.getvalue())

    def test_show_right_weapon(self):
        expected = 'right hand has weapon Sword\n'
        self.human.show_right_weapon()
        sys.stdout = sys.__stdout__
        self.assertEqual(expected, self.captured_output.getvalue())

    def test_show_left_weapon(self):
        expected = 'left hand has weapon Gun\n'
        self.human.show_left_weapon()
        sys.stdout = sys.__stdout__
        self.assertEqual(expected, self.captured_output.getvalue())

    def test_invoke_golem(self):
        expected = 'invoked golem\n'
        self.human.invoke_golem()
        sys.stdout = sys.__stdout__
        self.assertEqual(expected, self.captured_output.getvalue())


if __name__ == '__main__':
    unittest.main()
