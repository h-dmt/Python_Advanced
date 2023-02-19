
def shop_from_grocery_list(budget, shop_list, *args):
    output_print = []
    for elem in args:
        if elem[0] in shop_list:
            if budget >= elem[1]:
                shop_list.remove(elem[0])
                budget -= elem[1]
            else:
                break

    if len(shop_list) == 0:
        return f"Shopping is successful. Remaining budget: {budget:.2f}."
    else:
        return f"You did not buy all the products. Missing products: {', '.join(shop_list)}."




print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))
