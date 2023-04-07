from project.truck_driver import TruckDriver

from unittest import TestCase, main


class TestTruckDriver(TestCase):
    def setUp(self) -> None:
        self.driver = TruckDriver("Pino", 100)

    def test_init(self):
        self.assertEqual(self.driver.name, "Pino")
        self.assertEqual(self.driver.money_per_mile, 100)
        self.assertEqual(self.driver.available_cargos, {})
        self.assertEqual(self.driver.earned_money, 0)
        self.assertEqual(self.driver.miles, 0)

    def test_repr_output(self):
        self.assertEqual(self.driver.__repr__(), f"Pino has 0 miles behind his back.")

    def test_add_cargo_offer_cargo_already_added(self):
        self.driver.add_cargo_offer("Sofia", 500)
        with self.assertRaises(Exception) as ex:
            self.driver.add_cargo_offer("Sofia", 500)
        self.assertEqual(str(ex.exception), "Cargo offer is already added.")

    def test_add_cargo_added_and_return_message(self):
        result = self.driver.add_cargo_offer("Sofia", 500)
        self.assertEqual(result, "Cargo for 500 to Sofia was added as an offer.")
        self.assertEqual(self.driver.available_cargos, {"Sofia": 500})

    def test_drive_best_offer__no_offers(self):
        result = self.driver.drive_best_cargo_offer()
        self.assertEqual(result, "There are no offers available.")

    def test_driver_went_bankrupt(self):
        driver = TruckDriver("Pino", 1)
        driver.add_cargo_offer("Sofia", 500)
        driver.add_cargo_offer("Magadan", 12000)
        with self.assertRaises(ValueError) as ve:
            driver.drive_best_cargo_offer()
        self.assertEqual(str(ve.exception), "Pino went bankrupt.")

    def test_drive_best_offer_variables(self):
        self.driver.add_cargo_offer("Sofia", 500)
        self.driver.add_cargo_offer("Magadan", 12000)
        self.driver.drive_best_cargo_offer()
        self.assertEqual(self.driver.miles, 12000)
        self.assertEqual(self.driver.earned_money, 1187000)

    def test_drive_best_offer_output(self):
        self.driver.add_cargo_offer("Sofia", 500)
        self.driver.add_cargo_offer("Magadan", 12000)
        result = self.driver.drive_best_cargo_offer()
        self.assertEqual(result, "Pino is driving 12000 to Magadan.")

    def test_check_for_activities_eat(self):
        self.driver.add_cargo_offer("Sofia", 500)
        self.driver.drive_best_cargo_offer()
        self.assertEqual(49960, self.driver.earned_money)

    def test_check_for_activities_sleep(self):
        self.driver.add_cargo_offer("Slovenia", 1000)
        self.driver.drive_best_cargo_offer()
        self.assertEqual(99875, self.driver.earned_money)

    def test_check_for_activities_pump_gas(self):
        self.driver.add_cargo_offer("Milano", 1500)
        self.driver.drive_best_cargo_offer()
        self.assertEqual(149335, self.driver.earned_money)

    def test_check_for_activities_repair_truck(self):
        self.driver.add_cargo_offer("Moskow", 10000)
        self.driver.drive_best_cargo_offer()
        self.assertEqual(988250, self.driver.earned_money)


if __name__ == "__main__":
    main()
