from project.product import Product


class Drink(Product):
    QUANTITY = 10

    def __init__(self, name: str, quantity=QUANTITY):
        super().__init__(name, quantity)
        self.name = name
