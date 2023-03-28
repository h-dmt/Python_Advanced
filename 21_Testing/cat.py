class Cat:

    def __init__(self, name):
        self.name = name
        self.fed = False
        self.sleepy = False
        self.size = 0

    def eat(self):
        if self.fed:
            raise Exception('Already fed.')

        self.fed = True
        self.sleepy = True
        self.size += 1

    def sleep(self):
        if not self.fed:
            raise Exception('Cannot sleep while hungry')

        self.sleepy = False


import unittest


class CatTests(unittest.TestCase):

    def setUp(self) -> None:
        self.cat = Cat('Lilly')

    def test_size_after_eat(self):
        size0 = self.cat.size
        self.cat.eat()
        size1 = self.cat.size
        self.assertEqual(size1, size0 + 1)

    def test_fed_after_eat(self):
        self.cat.eat()
        fed = self.cat.fed
        self.assertTrue(fed)

    def test_eat_fed_error(self):
        self.cat.eat()
        with self.assertRaises(Exception) as context:
            self.cat.eat()
        self.assertEqual(str(context.exception), 'Already fed.')

    def test_no_fed__no_sleep(self):
        with self.assertRaises(Exception) as context:
            self.cat.sleep()
        self.assertEqual(str(context.exception), 'Cannot sleep while hungry')

    def test_not_sleepy_after_sleep(self):
        self.cat.eat()
        self.cat.sleep()
        sleepy = self.cat.sleepy
        self.assertFalse(sleepy)


if __name__ == '__main__':
    unittest.main()

