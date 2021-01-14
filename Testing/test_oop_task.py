import unittest

from oop_task import Monkey

class ExtendedMonkeyTestCase(unittest.TestCase):
    def setUp(self):
        self.default_name = "Dummy"
        self.new_name = "New One"
        self.default_age = 3
        self.new_age = 5
        self.default_actions = ['saying "Boo boo boo"', "sleeping", "eating"]
        self.new_actions = ["dreaming", "fighting", "eating"]
        self.monkey = Monkey(self.default_name, self.default_age, self.default_actions)

    def tearDown(self):
        del self.monkey

    def test_01_naming_default(self):
        self.assertEqual(self.monkey.name, self.default_name)

    def test_02_naming_new(self):
        self.monkey.set_name(self.new_name)
        self.assertEqual(self.monkey.name, self.new_name)

    def test_03_aging_default(self):
        self.assertEqual(self.monkey.age, self.default_age)

    def test_04_aging_new(self):
        self.monkey.set_age(self.new_age)
        self.assertEqual(self.monkey.age, self.new_age)

    @staticmethod
    def _get_all_possible_actions(monkey, actions):
        return [f"{monkey.name} is {x}" for x in actions]

    def test_05_action_default(self):
        self.assertIn(
            self.monkey.action(),
            self._get_all_possible_actions(self.monkey, self.default_actions),
        )

    def test_06_action_new(self):
        self.monkey.set_actions(self.new_actions)
        self.assertIn(
            self.monkey.action(),
            self._get_all_possible_actions(self.monkey, self.new_actions),
        )

suite = unittest.TestLoader().loadTestsFromModule(ExtendedMonkeyTestCase())
unittest.TextTestRunner().run(suite)