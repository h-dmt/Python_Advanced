"""
You are tasked to visualize a snake's zigzag path in a rectangular matrix with a size N x M.
A string represents the snake. It starts moving from the top-left corner to the right.
When the snake reaches the end of the row, it slithers its way down to the next row and turns left.
The moves are repeated to the very end.
The first cell is filled with the first symbol of the snake. The second cell is filled with the second
 symbol, etc. The snake's path is as long as it takes to fill the matrix completely - if you reach
 the end of the string representing the snake, start again at the first symbol. In the end,
 you should print the snake's path.
Input
The input data consists of exactly two lines:
    • On the first line, you will receive the dimensions N x M of the field in format: "{rows} {columns}".
    • On the second line, you will receive the string representing the snake
"""
from collections import deque

rows, columns = [int(x) for x in input().split()]
word = deque(input())
symb = ''
Matrix = []
r = []
for row in range(rows):
    while len(r) < columns:
        symb = word.popleft()
        r.append(symb)
        word.append(symb)
    if row % 2 == 0:
        Matrix.append(r.copy())
        r.clear()
    elif row % 2 != 0:
        r.reverse()
        Matrix.append(r.copy())
        r.clear()
[print(''.join(m)) for m in Matrix]
