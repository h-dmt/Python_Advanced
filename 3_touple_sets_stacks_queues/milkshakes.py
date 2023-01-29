"""
Input
    • On the first line of input, you will receive the integers representing the chocolate, separated by  ", ".
    • On the second line of input, you will receive the integers representing the cups of milk, separated by ", ".
Output
    • On the first line, print:
        ◦ If you successfully made 5 milkshakes: "Great! You made all the chocolate milkshakes needed!"
        ◦ Otherwise: "Not enough milkshakes."
    • On the second line - print:
        ◦ If there are chocolates left: "Chocolate: {chocolate1}, {chocolate2}, (…)"
        ◦ Otherwise: "Chocolate: empty"
    • On the third line - print:
        ◦ If there are cups of milk left: "Milk: {milk1}, {milk2}, {milk3}, (…)"
        ◦ Otherwise: "Milk: empty"
"""
from collections import deque

chocolate = deque(int(c) for c in input().split(', '))
milk = deque(int(m) for m in input().split(', '))

milkshakes = 0

while milkshakes < 5 and chocolate and milk:
    # check values ok
    if chocolate[-1] <= 0 and milk[-1] <= 0:
        chocolate.pop()
        milk.popleft()
        continue
    if chocolate[-1] <= 0:
        chocolate.pop()
        continue
    if milk[0] <= 0:
        milk.popleft()
        continue
    if not chocolate or not milk:
        break

    if chocolate[-1] == milk[0]:  # make milkshake
        chocolate.pop()
        milk.popleft()
        milkshakes += 1
    else:
        milk.append(milk.popleft())
        chocolate[-1] -= 5

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
if chocolate:
    chocolate = list(map(str, chocolate))
    print(f"Chocolate: {', '.join(chocolate)}")
else:
    print("Chocolate: empty")
if milk:
    milk = list(map(str, milk))
    print(f"Milk: {', '.join(milk)}")
else:
    print("Milk: empty")
