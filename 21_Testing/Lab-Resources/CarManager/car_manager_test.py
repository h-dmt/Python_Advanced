from CarManager.car_manager import Car
import unittest


class CarTest(unittest.TestCase):
    def setUp(self) -> None:
        self.car = Car("Opel", "Corsa", 5, 45)

    def test_constructor_make(self):
        make = self.car.make
        self.assertEqual(make, 'Opel')

    def test_constructor_model(self):
        model = self.car.model
        self.assertEqual(model, 'Corsa')

    def test_constructor_fuel_consum(self):
        fuel_consum = self.car.fuel_consumption
        self.assertEqual(fuel_consum, 5)

    def test_constructor_fuel_capacity(self):
        fuel_capacity = self.car.fuel_capacity
        self.assertEqual(fuel_capacity, 45)

    def test_constructor_f_amount(self):
        f_amount = self.car.fuel_amount
        self.assertEqual(f_amount, 0)

    def test_valid_make(self):
        with self.assertRaises(Exception) as context:
            Car("", "Corsa", 5, 45)
        self.assertEqual(str(context.exception), "Make cannot be null or empty!")

    def test_valid_model(self):
        with self.assertRaises(Exception) as context:
            Car("Opel", "", 5, 45)
        self.assertEqual(str(context.exception), "Model cannot be null or empty!")

    def test_valid_fuel_consumption(self):
        with self.assertRaises(Exception) as context:
            Car("Opel", "Corsa", 0, 45)
        self.assertEqual(str(context.exception), "Fuel consumption cannot be zero or negative!")

    def test_valid_fuel_capacity(self):
        with self.assertRaises(Exception) as context:
            Car("Opel", "Corsa", 5, 0)
        self.assertEqual(str(context.exception), "Fuel capacity cannot be zero or negative!")

    def test_valid_fuel_amount(self):
        with self.assertRaises(Exception) as context:
            self.car.fuel_amount = -5
        self.assertEqual(str(context.exception), "Fuel amount cannot be negative!")

    def test_refuel_valid_value(self):
        with self.assertRaises(Exception) as context:
            self.car.refuel(0)
        self.assertEqual(str(context.exception), "Fuel amount cannot be zero or negative!")

    def test_refuel_fuel_increase(self):
        self.car.refuel(20)
        fuel = self.car.fuel_amount
        self.assertEqual(fuel, 20)

    def test_refuel_max_capacity(self):
        self.car.refuel(100)
        fuel = self.car.fuel_amount
        self.assertEqual(fuel, 45)

    def test_drive_fuel_amount(self):
        self.car.refuel(45)
        self.car.drive(100)
        remaining_fuel = self.car.fuel_amount
        self.assertEqual(remaining_fuel, 40)

    def test_drive_no_fuel(self):
        with self.assertRaises(Exception) as context:
            self.car.drive(50)
        self.assertEqual(str(context.exception), "You don't have enough fuel to drive!")


if __name__ == "__main__":
    unittest.main()
