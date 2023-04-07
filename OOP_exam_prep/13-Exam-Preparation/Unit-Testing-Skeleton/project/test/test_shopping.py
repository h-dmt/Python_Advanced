from project.shopping_cart import ShoppingCart
from unittest import TestCase, main


class TestShoppingCart(TestCase):
    def setUp(self) -> None:
        self.cart = ShoppingCart("Shop", 50)
        self.cart2 = ShoppingCart("Ing", 50)

    def test_init_(self):
        self.assertEqual("Shop", self.cart.shop_name)
        self.assertEqual(50, self.cart.budget)
        self.assertEqual({}, self.cart.products)

    def test_name_property_setter_only_letters(self):
        with self.assertRaises(ValueError) as ve:
            ShoppingCart("Shop1", 100)
        expected = "Shop must contain only letters and must start with capital letter!"
        self.assertEqual(expected, str(ve.exception))

    def test_name_property_setter_starts_with_capital(self):
        with self.assertRaises(ValueError) as ve:
            ShoppingCart("shop", 100)
        expected = "Shop must contain only letters and must start with capital letter!"
        self.assertEqual(expected, str(ve.exception))

    # Add_to_chart
    def test_ad_to_chart__price_greater_than_100(self):
        with self.assertRaises(ValueError) as ve:
            self.cart.add_to_cart("product", 120)
        expected = "Product product cost too much!"
        self.assertEqual(expected, str(ve.exception))

    def test_ad_to_chart__return(self):
        result = self.cart.add_to_cart("product", 30)
        self.assertEqual("product product was successfully added to the cart!", result)
        self.assertEqual(30, self.cart.products["product"])

    # Remove_from_chart
    def test_remove_from_chart__no_product_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.cart.remove_from_cart("product")
        expected = f"No product with name product in the cart!"
        self.assertEqual(expected, str(ve.exception))

    def test_remove_from_chart__return(self):
        self.cart.add_to_cart("scarf", 25)
        self.cart.add_to_cart("shoes", 25)
        result = self.cart.remove_from_cart("scarf")
        self.assertEqual("Product scarf was successfully removed from the cart!", result)
        self.assertEqual({"shoes": 25}, self.cart.products)

    # __add__
    def test_add__new_shop_name_new_budget(self):
        self.cart.add_to_cart("scarf", 25)
        self.cart2.add_to_cart("shoes", 30)
        new_cart = self.cart.__add__(self.cart2)
        self.assertEqual("ShopIng", new_cart.shop_name)
        self.assertEqual(100, new_cart.budget)

    def test_add__new_shop_product_update(self):
        self.cart.add_to_cart("scarf", 25)
        self.cart2.add_to_cart("shoes", 30)
        new_cart = self.cart.__add__(self.cart2)
        self.assertEqual({"scarf": 25, "shoes": 30}, new_cart.products)

    def test_add__new_shop_return(self):
        self.cart.add_to_cart("scarf", 25)
        result = self.cart.__add__(self.cart2)
        self.assertEqual(result.__class__.__name__, self.cart.__add__(self.cart2).__class__.__name__)

    # buy products
    def test_buy_products__return_ok(self):
        self.cart.add_to_cart("scarf", 15)
        self.cart.add_to_cart("shoes", 25)
        result = self.cart.buy_products()
        expected = 'Products were successfully bought! Total cost: 40.00lv.'
        self.assertEqual(expected, result)

    def test_buy_products__not_enough_budget_value_error(self):
        self.cart.add_to_cart("scarf", 15)
        self.cart.add_to_cart("shoes", 50)
        with self.assertRaises(ValueError) as ve:
            self.cart.buy_products()
        expected = "Not enough money to buy the products! Over budget with 15.00lv!"
        self.assertEqual(expected, str(ve.exception))


if __name__ == "__main__":
    main()