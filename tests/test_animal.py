import unittest
import sys
sys.path.append('../')
from animals import Animal
from animals import Dog


class TestAnimal(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.bob = Dog("Bob")
        self.jacob = Animal("Jacob")

    def test_animal_creation(self):

        murph = Dog("Murph")

        self.assertIsInstance(murph, Dog)
        self.assertIsInstance(murph, Animal)
        self.assertIsInstance(self.jacob, Animal)

    def test_animal_can_set_legs(self):
        self.bob.set_legs(6)
        self.assertEqual(self.bob.legs, 6)

    def test_animal_can_get_species(self):
        self.assertIs(self.bob.get_species(), "Dog")

    def test_animal_can_set_species(self):
        self.bob.set_species("Poodle")
        self.assertIs(self.bob.species, "Poodle")

    def test_animal_can_walk(self):
        self.bob.set_legs(6)
        self.bob.walk()
        self.assertEqual(self.bob.speed, 1.20)

    def test_animal_get_name(self):
        self.assertEqual(self.bob.name, "Bob")


if __name__ == '__main__':
    unittest.main()




