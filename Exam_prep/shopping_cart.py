"""
Write a function called that adds products to a shopping cart for the following three types of meals:
"Soup", "Pizza", and "Dessert". Every meal has a limit of products that can be added to it:
    • Soup: 3
    • Pizza: 4
    • Dessert: 2
Once you reach the limit of a meal, you should stop adding products to that meal.
The function will receive a different number of arguments. The arguments will be passed as tuples with two elements
- the first one is the type of meal, and the second is the product for the meal.
You need to take each argument and make a dictionary with the meal's name as a key and the products as a value
of the corresponding key.
There are some additional requirements:
    • If you receive the same product for the same meal more than once, you must not add it again.
    • If you run into the word "Stop" (not tuple) as an argument, you must immediately stop adding products to
    the cart - just sort and return the desired result as described below.
In the end, sort the meals by the number of bought products in descending order.
If there are meals with an equal number of products, sort them (the meals) by their name in ascending order
(alphabetically). For each meal sort its products in ascending order (alphabetically).
"""


def shopping_cart(*args):
    meals = {"Soup": list(), "Pizza": list(), "Dessert": list()}
    products_limit = {"Soup": 3, "Pizza": 4, "Dessert": 2}
    output = []
    empty_cart = True
    for arg in args:
        if arg != 'Stop':
            meal = arg[0]
            product = arg[1]
            if meal in meals and len(meals[meal]) < products_limit[meal] and product not in meals[meal]:
                meals[meal].append(product)
                empty_cart = False
        else:
            break

    sorted_cart = dict(sorted(meals.items(), key=lambda x: (-len(x[1]), x[0])))
    for k in sorted_cart:
        output.append(f"{k}:")
        for v in sorted(sorted_cart[k]):
            output.append(f" - {v}")

    if not empty_cart:
        return '\n'.join(output)
    else:
        return "No products in the cart!"


print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))