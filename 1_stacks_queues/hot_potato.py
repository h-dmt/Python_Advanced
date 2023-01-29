"""
Every nth toss, the child holding the potato leaves the game. When a
kid leaves the game, it passes the potato to the next kid. It continues until there is only
one kid left.
Create a program that simulates the game of Hot Potato. On the first line, you will receive
kids' names, separated by a single space. On the second line, you will receive the nth toss
(integer) in which a child leaves the game.
Print every kid who is removed from the circle in the format "Removed {kid}". In the end,
print the only kid left in the format "Last is {kid}".
"""

from collections import deque

names = input().split(' ')
players = deque(names)
toss = int(input())

while len(players) > 1:
    for _ in range(toss):
        players.append(players.popleft())

    print(f"Removed {players.pop()}")
print(f"Last is {players.popleft()}")
