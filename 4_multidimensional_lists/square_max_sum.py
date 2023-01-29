"""
Write a program that reads a matrix from the console and finds the 2x2 top-left submatrix
with biggest sum of its values.
On first line you will get matrix sizes in format "{rows}, {columns}".
On the next rows, you will get elements for each column, separated with a comma and a space ", ".
You should print the found submatrix and the sum of its elements, as shown in the examples.
"""


def sum_sub_matrix(matrix):
    sum_els = 0
    for r in matrix:
        for el in r:
            sum_els += el
    return sum_els


rows, columns = [int(x) for x in input().split(', ')]
M = [[int(m) for m in input().split(', ')] for _ in range(rows)]

sub_M = []
max_sum = 0
max_sub_M = []
for row in range(rows - 1):
    for col in range(columns - 1):
        sub_M = [[M[row][col], M[row][col + 1]], [M[row + 1][col], M[row + 1][col + 1]]]
        sum_sub = sum_sub_matrix(sub_M)
        if sum_sub > max_sum:
            max_sum = sum_sub
            max_sub_M = sub_M
[print(*r) for r in max_sub_M]
print(max_sum)
