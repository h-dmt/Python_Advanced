# https://judge.softuni.org/Contests/Practice/Index/2812#2
from collections import deque


def stock_availability(inventory, action, *args):
    n = int()
    inventory = deque(inventory)
    if action == 'delivery':
        for product in args:
            inventory.append(product)

    elif action == 'sell':

        if len(args) == 1 and isinstance(args[0], int):
            n = args[0]
            for _ in range(n):
                inventory.popleft()
                if len(inventory) == 0:
                    break
        elif len(args) >= 1:
            for el in args:
                while el in inventory:
                    inventory.remove(el)
        else:
            inventory.popleft()

    return list(inventory)


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 9))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
