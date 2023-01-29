"""
Write a program that reads a matrix from the console and prints the sum for each column
on separate lines.
On the first line, you will get matrix sizes in format "{rows}, {columns}".
On the next rows, you will get
elements for each column separated with a single space.
"""

rows, columns = [x for x in list((map(int, input().split(', '))))]
M = [[int(m) for m in input().split(' ')] for _ in range(rows)]
col_sum = 0
cols = []
for c in range(columns):
    for r in range(rows):
        col_sum += M[r][c]
    cols.append(col_sum)
    col_sum = 0
print(*cols, sep='\n')
