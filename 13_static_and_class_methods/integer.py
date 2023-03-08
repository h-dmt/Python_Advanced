import unittest


class Integer:
    def __init__(self, value: int):
        self.value = value

    @classmethod
    def from_float(cls, float_value: float):

        if not isinstance(float_value, float):
            return "value is not a float"

        else:
            return cls(int(float_value))

    @classmethod
    def from_roman(cls, value: str):
        roman_n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result_int = roman_n[value[0]]

        for i in range(1, len(value)):

            if roman_n[value[i]] > roman_n[value[i-1]]:
                result_int += roman_n[value[i]] - 2 * roman_n[value[i-1]]

            else:
                result_int += roman_n[value[i]]

        return cls(result_int)

    @classmethod
    def from_string(cls, str_value: str):

        if isinstance(str_value, str):
            if str_value.isnumeric():
                return cls(int(str_value))

        return "wrong type"


first_num = Integer(10)
print(first_num.value)

second_num = Integer.from_roman("IV")
print(second_num.value)

print(Integer.from_float(7.8))
print(Integer.from_string("2"))

class IntegerTests(unittest.TestCase):
    def test_basic_init(self):
        integer = Integer(1)
        self.assertEqual(integer.value, 1)

    def test_from_float_success(self):
        integer = Integer.from_float(2.5)
        self.assertEqual(integer.value, 2)

    def test_from_float_wrong_type(self):
        result = Integer.from_float("2.5")
        self.assertEqual(result, "value is not a float")

    def test_from_roman(self):
        integer = Integer.from_roman("XIX")
        self.assertEqual(integer.value, 19)

    def test_from_string_success(self):
        integer = Integer.from_string("10")
        self.assertEqual(integer.value, 10)

    def test_from_string_wrong_type(self):
        result = Integer.from_string(1.5)
        self.assertEqual(result, "wrong type")


if __name__ == "__main__":
    unittest.main()