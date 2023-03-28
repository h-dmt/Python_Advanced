from extended_list import IntegerList
import unittest


class ListTest(unittest.TestCase):

    def setUp(self) -> None:
        self.integer_list = IntegerList(1, 'r', 4, 2, 5)

    def test_constructor_empty(self):
        empty_list = IntegerList()
        self.assertEqual(empty_list.get_data(), [])

    def test_constructor(self):
        data = self.integer_list.get_data()
        self.assertEqual(data, [1, 4, 2, 5])

    def test_add(self):
        self.integer_list.add(3)
        data = self.integer_list.get_data()
        self.assertEqual(data, [1, 4, 2, 5, 3])

    def test_add_value_error(self):
        with self.assertRaises(ValueError) as context:
            self.integer_list.add('3')
        self.assertEqual(str(context.exception), "Element is not Integer")

    def test_remove_index(self):
        self.integer_list.remove_index(0)
        data = self.integer_list.get_data()
        self.assertEqual(data, [4, 2, 5])

    def test_remove_index_error(self):
        with self.assertRaises(IndexError) as context:
            self.integer_list.remove_index(9)
        self.assertEqual(str(context.exception), "Index is out of range")

    def test_init_only_integers(self):
        data = self.integer_list.get_data()
        all_integers = all(type(x) == int for x in data)
        self.assertTrue(all_integers)

    def test_init_data(self):
        data = self.integer_list.get_data()
        self.assertEqual(data, [1, 4, 2, 5])

    def test_get_element(self):
        el = self.integer_list.get(0)
        self.assertEqual(el, 1)

    def test_get_index_range(self):
        with self.assertRaises(IndexError) as context:
            self.integer_list.get(9)
        self.assertEqual(str(context.exception), "Index is out of range")

    def test_insert(self):
        self.integer_list.insert(0, 9)
        data = self.integer_list.get_data()
        self.assertEqual(data, [9, 1, 4, 2, 5])

    def test_insert_index_range_error(self):
        with self.assertRaises(IndexError) as context:
            self.integer_list.insert(7, 3)
        self.assertEqual(str(context.exception), "Index is out of range")

    def test_insert_index_element_is_int(self):
        with self.assertRaises(ValueError) as context:
            self.integer_list.insert(1, '2')
        self.assertEqual(str(context.exception), "Element is not Integer")

    def test_get_biggest(self):
        biggest = self.integer_list.get_biggest()
        self.assertEqual(biggest, 5)

    def test_get_index(self):
        index = self.integer_list.get_index(5)
        self.assertEqual(index, 3)


if __name__ == "__main__":
    unittest.main()
