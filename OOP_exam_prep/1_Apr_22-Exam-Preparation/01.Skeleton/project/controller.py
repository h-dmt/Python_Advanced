from typing import List

from project.car.car import Car
from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:
    def __init__(self):
        self.cars: List[Car] = []
        self.drivers: List[Driver] = []
        self.races: List[Race] = []

    def create_car(self, car_type: str, model: str, speed_limit: int) -> str:
        if [car for car in self.cars if car.model == model]:
            raise Exception(f"Car {model} is already created!")

        valid_type_of_car = {"MuscleCar": MuscleCar, "SportsCar": SportsCar}
        if car_type in valid_type_of_car:

            new_car = valid_type_of_car[car_type](model, speed_limit)
            self.cars.append(new_car)

            return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str) -> str:
        if [driver for driver in self.drivers if driver.name == driver_name]:
            raise Exception(f"Driver {driver_name} is already created!")

        new_driver = Driver(driver_name)
        self.drivers.append(new_driver)
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str) -> str:
        if [race for race in self.races if race.name == race_name]:
            raise Exception(f"Race {race_name} is already created!")

        new_race = Race(race_name)
        self.races.append(new_race)
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str) -> str:
        try:
            driver = next(filter(lambda d: d.name == driver_name, self.drivers))
        except StopIteration:
            raise Exception(f"Driver {driver_name} could not be found!")

        valid_types = {"MuscleCar": MuscleCar, "SportsCar": SportsCar}

        try:
            car = next(filter(lambda c: type(c) == valid_types[car_type] and not c.is_taken, reversed(self.cars)))
        except StopIteration:
            raise Exception(f"Car {car_type} could not be found!")

        if driver.car:
            old_car = driver.car
            old_car.is_taken = False
            driver.car = car
            car.is_taken = True
            return f"Driver {driver_name} changed his car from {old_car.model} to {car.model}."

        else:
            driver.car = car
            car.is_taken = True
            return f"Driver {driver_name} chose the car {car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str) -> str:
        try:
            race = next(filter(lambda r: r.name == race_name, self.races))
        except StopIteration:
            raise Exception(f"Race {race_name} could not be found!")

        try:
            driver = next(filter(lambda d: d.name == driver_name, self.drivers))
        except StopIteration:
            raise Exception(f"Driver {driver_name} could not be found!")

        if [d for d in race.drivers if d.name == driver_name]:
            return f"Driver {driver_name} is already added in {race_name} race."

        if driver.car:
            race.drivers.append(driver)
            return f"Driver {driver_name} added in {race_name} race."

        else:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

    def start_race(self, race_name: str) -> str:
        try:
            race = next(filter(lambda r: r.name == race_name, self.races))
        except StopIteration:
            raise Exception(f"Race {race_name} could not be found!")

        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        participant_cars = [d.car for d in race.drivers]
        cars_sorted_by_speed = sorted(participant_cars, key=lambda car: car.speed_limit, reverse=True)
        output_print = []
        for i in range(3):
            fastest_car = cars_sorted_by_speed[i]
            fastest_driver = next(filter(lambda d: d.car == fastest_car, self.drivers))
            fastest_driver.number_of_wins += 1
            output_print.append(f"Driver {fastest_driver.name} wins the {race_name} race"
                                f" with a speed of {fastest_car.speed_limit}.")

        return "\n".join(output_print)
