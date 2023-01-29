"""
here is a circle road with N petrol pumps. The petrol pumps are numbered 0 to (N−1)
(both inclusive). For each petrol pump, you will receive two pieces of information
(separated by a single space):
    • The amount of petrol the petrol pump will give you
    • The distance from that petrol pump to the next petrol pump (kilometers)
You are a truck driver, and you want to go all around the circle. You know that the
truck consumes 1 liter of petrol per 1 kilometer, and its tank has infinite petrol
capacity.

In the beginning, the tank is empty, but you start your journey at a petrol pump so you can fill it with the given
amount of petrol.
Your task is to calculate the first petrol pump from where the truck will be able to complete the circle.
You never miss filling its tank at a petrol pump.
Input
    • On the first line, you will receive the number of petrol pumps - N
    • On the next N lines, you will receive the amount of petrol that each petrol
    pump will give and the distance between that petrol pump and the next
    petrol pump, separated by a single space

"""
from collections import deque
indexes = deque(ind for ind in range(int(input())))
stations = {n: list(map(int, input().split())) for n in range(len(indexes))}
f_on_board = 0
index_copy = indexes.copy()

while index_copy:
    fuel, distance = stations[index_copy.popleft()]
    f_on_board += fuel
    if f_on_board >= distance:
        f_on_board -= distance
    else:
        indexes.append(indexes.popleft())
        index_copy = indexes.copy()
        f_on_board = 0
print(indexes[0])
