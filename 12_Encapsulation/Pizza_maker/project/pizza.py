from project.dough import Dough
from project.topping import Topping


class Pizza:
    def __init__(self, name: str, dough: Dough, max_number_of_toppings: int, toppings={}):
        self.name = name
        self.dough = dough
        self.max_number_of_toppings = max_number_of_toppings
        self.toppings = toppings  # {topping type: topping's weight}
        self.added_toppings = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) == 0:
            raise ValueError("The name cannot be an empty string")

        self.__name = value

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, value):
        if value is None:
            raise ValueError("You should add dough to the pizza")

        self.__dough = value

    @property
    def max_number_of_toppings(self):
        return self.__max_number_of_toppings

    @max_number_of_toppings.setter
    def max_number_of_toppings(self, value):
        if value <= 0:
            raise ValueError("The maximum number of toppings cannot be less or equal to zero")

        self.__max_number_of_toppings = value

    def add_topping(self, topping: Topping) -> [str, None]:
        # ◦ Add a new topping to the dictionary
        # • If there is no space left for a new topping, raise a ValueError: "Not enough space for another topping"
        # • If the topping is already in the dictionary, increase the value of its weight.

        if self.added_toppings == self.max_number_of_toppings:
            raise ValueError("Not enough space for another topping")

        elif topping.topping_type in self.toppings:
            self.toppings[topping.topping_type] += topping.weight
            self.added_toppings += 1

        else:
            self.toppings[topping.topping_type] = topping.weight
            self.added_toppings += 1

    def calculate_total_weight(self):
        # returns the total weight of the pizza (dough's weight and toppings' weight)

        topping_weight = 0
        dough_weight = self.dough.weight
        for topping in self.toppings:
            topping_weight += self.toppings[topping]

        return dough_weight + topping_weight
