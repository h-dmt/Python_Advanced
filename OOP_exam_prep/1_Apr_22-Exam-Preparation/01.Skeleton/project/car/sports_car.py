from project.car.car import Car


class SportsCar(Car):
    MIN_SPEED = 400
    MAX_SPEED = 600

    @property
    def speed_limit(self):
        return self.__speed_limit

    @speed_limit.setter
    def speed_limit(self, value):
        if value < self.MIN_SPEED or value > self.MAX_SPEED:
            raise ValueError(f"Invalid speed limit! Must be between {self.MIN_SPEED} and {self.MAX_SPEED}!")
        self.__speed_limit = value
