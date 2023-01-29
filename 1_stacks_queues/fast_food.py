"""
First, you will be given the quantity of the food you have for the day (an integer number). Next, you will be given
 a sequence of integers (separated by a single space), each representing the quantity of food in each order.
 Keep the orders in a queue.
Find the biggest order and print it. Next, you will begin servicing your clients from the first one that came.
Before each order, check if you have enough food left to complete it:
    • If you have, remove the order from the queue and reduce the quantity of food in the restaurant.
    • Otherwise, stop serving.
Input
    • On the first line, you will be given the quantity of your food - an integer in the range [0, 1000]
    • On the second line, you will receive a sequence of integers, representing each order, separated by a single space
Output
    • On the first line, print the quantity of the biggest order
    • On the second line:
        ◦ If you succeeded in servicing all your clients, print: "Orders complete".
        ◦ Otherwise, print: "Orders left: {order1} {order2} .... {orderN}".
"""
from collections import deque

qty = int(input())
orders = deque([int(n) for n in input().split()])
print(max(orders))

for order in orders.copy():  # using a copy of orders, because orders changes sizes during iterations

    if order <= qty:
        orders.popleft()
        qty -= order
    else:
        print(f"Orders left: {' '.join([str(o) for o in orders])}")
        break
if not orders:
    print("Orders complete")
