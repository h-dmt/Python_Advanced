from project.product import Product


class Food(Product):
    QUANTITY = 15

    def __init__(self, name: str, quantity=15):
        super().__init__(name, quantity)
        self.name = name
