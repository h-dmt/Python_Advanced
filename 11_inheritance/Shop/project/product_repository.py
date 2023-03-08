from typing import List

from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str) -> None:
        try:
            name = next(filter(lambda n: n.name == product_name, self.products))
        except StopIteration:
            return

        if name:
            return name

    def remove(self, product_name: str) -> None:
        try:
            name = next(filter(lambda n: n.name == product_name, self.products))
        except StopIteration:
            return

        if name:
            self.products.remove(name)

    def __repr__(self):
        out_print = []
        for prod in self.products:
            out_print.append(f"{prod.name}: {prod.quantity}")

        return '\n'.join(out_print)
