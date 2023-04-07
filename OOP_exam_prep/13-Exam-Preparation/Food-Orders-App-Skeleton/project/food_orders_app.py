from typing import List

from project.client import Client
from project.meals.dessert import Dessert
from project.meals.main_dish import MainDish
from project.meals.meal import Meal
from project.meals.starter import Starter


class FoodOrdersApp:
    def __init__(self):
        self.menu: List[Meal] = []
        self.clients_list: List[Client] = []
        self.receipt_id = 0

    def register_client(self, client_phone_number: str) -> str:

        if [c for c in self.clients_list if c.phone_number == client_phone_number]:
            raise Exception("The client has already been registered!")

        client = Client(client_phone_number)
        self.clients_list.append(client)
        return f"Client {client.phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal) -> None:

        valid_meals = (Starter, MainDish, Dessert)
        for m in meals:
            if isinstance(m, valid_meals):
                self.menu.append(m)

    def show_menu(self) -> str:

        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        menu_details = []
        for meal in self.menu:
            menu_details.append(meal.details())

        return "\n".join(menu_details)

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities) -> str:

        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        client = [c for c in self.clients_list if c.phone_number == client_phone_number]
        if not client:
            self.register_client(client_phone_number)
            client = [c for c in self.clients_list if c.phone_number == client_phone_number]

        client = client[0]
        current_bill = 0
        current_shopping_cart = []
        # Check for exceptions!
        for meal_name, qty in meal_names_and_quantities.items():

            # First check if meal is in the menu
            try:
                meal = next(filter(lambda m: m.name == meal_name, self.menu))
            except StopIteration:
                raise Exception(f"{meal_name} is not on the menu!")

            # Check enough quantity
            if qty > meal.quantity:
                raise Exception(f"Not enough quantity of {meal.__class__.__name__}: {meal_name}!")

            meal_type = type(meal)
            meal.quantity -= qty
            cart_meal = meal_type(meal_name, meal.price, qty)
            current_shopping_cart.append(cart_meal)
            current_bill += meal.price * qty

        # complete adding meals to cart ...
        client.shopping_cart.extend(current_shopping_cart)
        client.bill += current_bill
        meal_names = []
        for meal_in_cart in client.shopping_cart:
            if meal_in_cart.name not in meal_names:
                meal_names.append(meal_in_cart.name)

        return f"Client {client_phone_number} successfully ordered {', '.join(meal_names)} for {client.bill:.2f}lv."

    def cancel_order(self, client_phone_number: str) -> str:

        client = next(filter(lambda c: c.phone_number == client_phone_number, self.clients_list))
        if len(client.shopping_cart) == 0:
            raise Exception("There are no ordered meals!")

        self.empty_cart(client)

        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str) -> str:
        client = next(filter(lambda c: c.phone_number == client_phone_number, self.clients_list))

        if len(client.shopping_cart) == 0:
            raise Exception("There are no ordered meals!")

        del client.shopping_cart[:]
        total_paid_money = client.bill
        client.bill = 0
        self.receipt_id += 1
        return f"Receipt #{self.receipt_id} with total amount of {total_paid_money:.2f} " \
               f"was successfully paid for {client_phone_number}."

    def __str__(self):
        number_of_listed_meals = len(self.menu)
        number_of_clients = len(self.clients_list)
        return f"Food Orders App has {number_of_listed_meals} meals on the menu and {number_of_clients} clients."

    def empty_cart(self, client):
        for meal_in_cart in list(client.shopping_cart):
            meal = next(filter(lambda m: m.name == meal_in_cart.name, self.menu))
            meal.quantity += meal_in_cart.quantity
            client.bill -= meal.price * meal_in_cart.quantity
            client.shopping_cart.remove(meal_in_cart)


