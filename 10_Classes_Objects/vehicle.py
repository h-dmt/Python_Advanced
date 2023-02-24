# Create a class called Vehicle. Upon initialization, it should receive max_speed
# (integer, optional; 150 by default) and mileage (number). Create an instance variable called gadgets
# - an empty list by default.

class Vehicle:
    def __init__(self, mileage: int, max_speed=150):
        self.gadgets = []
        self.mileage = mileage
        self.max_speed = max_speed

    def mileage(self):
        return self.mileage

    def max_speed(self):
        return self.max_speed

    def car_gadgets(self):
        return self.gadgets


car = Vehicle(20)
print(car.max_speed)
print(car.mileage)
print(car.gadgets)
car.gadgets.append('Hudly Wireless')
print(car.gadgets)
