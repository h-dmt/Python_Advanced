from project.mammal import Mammal
from unittest import TestCase, main


class TestMammal(TestCase):
    def setUp(self) -> None:
        self.mammal = Mammal("Ciccio", "dog", "woof")

    def test_init_structure(self):
        self.assertEqual(self.mammal.name, 'Ciccio')
        self.assertEqual(self.mammal.type, 'dog')
        self.assertEqual(self.mammal.sound, 'woof')

    def test_make_sound(self):
        self.assertEqual(self.mammal.make_sound(), "Ciccio makes woof")

    def test_get_kingdom(self):
        self.assertEqual(self.mammal.get_kingdom(), "animals")

    def test_info(self):
        self.assertEqual(self.mammal.info(), "Ciccio is of type dog")


if __name__ == "__main__":
    main()
