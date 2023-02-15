# https://judge.softuni.org/Contests/3596/Python-Advanced-Exam-22-October-2022

from collections import deque
ml_caffein = input().split(', ')
ml_caffein = deque(map(int, ml_caffein))
drinks = input().split(', ')
drinks = deque(map(int, drinks))
caffein_qty = 0
MAX_CAFFEIN = 300

while ml_caffein and drinks:
    ml = ml_caffein.pop()
    drink = drinks.popleft()
    if caffein_qty + ml * drink <= MAX_CAFFEIN:
        caffein_qty += ml * drink
    else:
        drinks.append(drink)
        caffein_qty -= 30
        if caffein_qty < 0:
            caffein_qty = 0
if drinks:
    print("Drinks left:", end=' ')
    print(*drinks, sep=', ')
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")
print(f"Stamat is going to sleep with {caffein_qty} mg caffeine.")
