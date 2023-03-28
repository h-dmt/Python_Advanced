from project.vehicle import Vehicle
from unittest import TestCase, main


class TestVehicle(TestCase):
    def setUp(self) -> None:
        self.vehicle = Vehicle(50, 100)

    def test_constructor(self):
        self.assertEqual(self.vehicle.fuel, 50)
        self.assertEqual(self.vehicle.fuel_consumption, 1.25)
        self.assertEqual(self.vehicle.capacity, 50)
        self.assertEqual(self.vehicle.horse_power, 100)

    def test_drive_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(100)
        self.assertEqual(str(ex.exception), "Not enough fuel")

    def test_drive_fuel_update(self):
        self.vehicle.drive(10)
        self.assertEqual(self.vehicle.fuel, 37.5)

    def test_refuel_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(20)
        self.assertEqual(str(ex.exception), "Too much fuel")

    def test_refuel_fuel_update(self):
        self.vehicle.drive(30)
        self.vehicle.refuel(20)
        self.assertEqual(self.vehicle.fuel, 32.5)

    def test_str_(self):
        self.assertEqual(self.vehicle.__str__(), "The vehicle has 100 horse power with "
                                                 "50 fuel left and 1.25 fuel consumption")


if __name__ == "__main__":
    main()
