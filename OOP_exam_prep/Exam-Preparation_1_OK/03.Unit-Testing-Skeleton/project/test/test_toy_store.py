from project.toy_store import ToyStore
from unittest import TestCase, main


class TestToyStore(TestCase):
    def setUp(self) -> None:
        self.store = ToyStore()

    def test_correct_init(self):
        for key in range(ord("A"), ord("G") + 1):
            self.assertIsNone(self.store.toy_shelf[chr(key)])

        # check len on dictionary
        self.assertEqual(len(self.store.toy_shelf), 7)

    def test_add_toy_not_existing_shelf_exception(self):
        with self.assertRaises(Exception) as ex:
            self.store.add_toy("Z", "toy")
        self.assertEqual(str(ex.exception), "Shelf doesn't exist!")

    def test_ad_toy_already_in_shelf_exception(self):
        self.store.add_toy("A", "toy")
        with self.assertRaises(Exception) as ex:
            self.store.add_toy("A", "toy")
        self.assertEqual(str(ex.exception), "Toy is already in shelf!")

    def test_add_toy_shelf_already_taken_exception(self):
        self.store.add_toy("A", "toy")
        with self.assertRaises(Exception) as ex:
            self.store.add_toy("A", "toy_2")
        self.assertEqual(str(ex.exception), "Shelf is already taken!")

    def test_add_toy_placed_successfully_string(self):
        result = self.store.add_toy("A", "toy")
        self.assertEqual(result, f"Toy:toy placed successfully!")
        self.assertEqual(self.store.toy_shelf["A"], "toy")

    def test_remove_toy_from_non_exist_shell_exeption(self):
        self.store.add_toy("A", "toy")

        with self.assertRaises(Exception) as ex:
            self.store.remove_toy("R", "toy")
        self.assertEqual(str(ex.exception), "Shelf doesn't exist!")

    def test_remove_not_existing_toy_exception(self):
        self.store.add_toy("A", "toy")
        self.store.remove_toy("A", "toy")
        with self.assertRaises(Exception) as ex:
            self.store.remove_toy("A", "toy")
        self.assertEqual(str(ex.exception), "Toy in that shelf doesn't exists!")

    def test_remove_correctly_output(self):
        self.store.add_toy("A", "toy")
        result = self.store.remove_toy("A", "toy")
        self.assertEqual(result, "Remove toy:toy successfully!")

    def test_remove_toy_removed(self):
        self.store.add_toy("A", "toy")
        self.store.remove_toy("A", "toy")
        self.assertEqual(self.store.toy_shelf["A"], None)


if __name__ == "__main__":
    main()
