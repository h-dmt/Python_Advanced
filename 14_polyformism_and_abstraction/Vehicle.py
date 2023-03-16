from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    COND = 0.9
    LOSS = 0

    def drive(self, distance):
        self.fuel_consumption += Car.COND
        if distance * self.fuel_consumption <= self.fuel_quantity:
            self.fuel_quantity -= distance * self.fuel_consumption

    def refuel(self, fuel):
        self.fuel_quantity += fuel * (1 - Car.LOSS)


class Truck(Vehicle):
    COND = 1.6
    LOSS = 0.05

    def drive(self, distance):
        self.fuel_consumption += Truck.COND
        if distance * self.fuel_consumption <= self.fuel_quantity:
            self.fuel_quantity -= distance * self.fuel_consumption

    def refuel(self, fuel):
        self.fuel_quantity += fuel * (1 - Truck.LOSS)


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)

truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
