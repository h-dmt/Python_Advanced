class Product:
    def __init__(self, name: str, quantity: int):
        self.name = name
        self.quantity = quantity

    def decrease(self, quantity: int) -> None:
        # decreases the quantity of the product only if there is enough
        if quantity <= self.quantity:
            self.quantity -= quantity

    def increase(self, quantity: int) -> None:
        # increases the quantity of the product
        self.quantity += quantity

    def __repr__(self):
        return self.name
