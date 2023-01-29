"""
Write a program to generate the following matrix of palindromes of 3 letters with
r rows and c columns like the one in the examples below.
    • Rows define the first and the last letter: row 0  'a', row 1  'b', row 2  'c', …
    • Columns + rows define the middle letter:
        ◦ column 0, row 0  'a', column 1, row 0  'b', column 2, row 0  'c', …
        ◦ column 0, row 1  'b', column 1, row 1  'c', column 2, row 1  'd', …
Input
    • The numbers r and c stay at the first line at the input in the format "{rows} {columns}"
    • r and c are integers in the range [1, 26]
"""

rows, columns = [int(a) for a in input().split()]
M = []
el = []
for row in range(rows):
    for col in range(columns):
        el.append(chr(row + 97) + chr(97 + row + col) + chr(row + 97))
    M.append(el.copy())
    el.clear()
[print(*m) for m in M]
