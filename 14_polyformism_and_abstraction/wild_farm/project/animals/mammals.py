from project.animals.animal import Mammal
from project.food import Vegetable, Fruit, Meat, Food


class Mouse(Mammal):
    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    @property
    def eats_food(self):
        return [Vegetable, Fruit]

    @property
    def gained_weight(self):
        return 0.10

    @staticmethod
    def make_sound():
        return "Squeak"


class Dog(Mammal):
    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    @property
    def eats_food(self):
        return [Meat]

    @property
    def gained_weight(self):
        return 0.40

    @staticmethod
    def make_sound():
        return "Woof!"


class Cat(Mammal):
    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    @property
    def eats_food(self):
        return [Meat, Vegetable]

    @property
    def gained_weight(self):
        return 0.30

    @staticmethod
    def make_sound():
        return "Meow"


class Tiger(Mammal):
    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    @property
    def eats_food(self):
        return [Meat]

    @property
    def gained_weight(self):
        return 1

    @staticmethod
    def make_sound():
        return "ROAR!!!"
