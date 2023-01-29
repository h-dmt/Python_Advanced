"""
You own a fashion boutique and receive a delivery of a huge box of clothes, represented as a sequence of integers.
On the following line, you will be given an integer representing the capacity for one rack in your store.
You must arrange the clothes in the store and use the racks to hang up every piece of clothing.
You start from the last piece of clothing on the top of the pile to the first one at the bottom. Use a stack
for this purpose. Each piece of clothing has its value (an integer). You must sum their values while you take
them out of the box:
    • If the sum becomes equal to the capacity of the current rack, you must take a new one for the next clothes
    (if there are any left in the box).
    • If the sum becomes greater than the capacity, do not hang the piece of clothing on the current rack.
    Take a new rack and then hang it up.
In the end, print how many racks you have used to hang up the clothes.
Input
    • On the first line, you will be given a sequence of integers representing the clothes in the box,
    separated by a single space.
    • On the second line, you will be given an integer representing the capacity of a rack.
Output
    • Print the number of racks needed to hang up the clothes from the box.
"""

from collections import deque


def order(clothes, rack_capacity):
    n_racks = 1
    curr_cloth = 0
    current_space = rack_capacity
    while clothes:
        curr_cloth = clothes.pop()
        current_space -= curr_cloth
        if current_space < 0:
            n_racks += 1
            current_space = rack_capacity
            clothes.append(curr_cloth)
    return n_racks


clothes = deque(map(int, input().split()))
rack_capacity = int(input())
n_racks = 0
if sum(clothes) > 0:
    n_racks = order(clothes, rack_capacity)

print(n_racks)
