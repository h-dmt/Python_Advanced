"""
Find the number of all 2x2 squares containing identical chars in a matrix.
On the first line, you will receive the matrix's dimensions in the format "{rows} {columns}".
On the following rows, you will receive characters separated by a single space. Print the number of
all square matrices you have found.
"""

r, c = [int(x) for x in input().split(' ')]
matrix = [[j for j in input().split(' ')] for _ in range(r)]
n_square_matrix = 0
uniq_symb = []
for row in range(r - 1):
    for col in range(c - 1):
        symb = matrix[row][col]
        if matrix[row][col+1] == symb and matrix[row+1][col] == symb and matrix[row+1][col+1] == symb:
            n_square_matrix += 1

print(n_square_matrix)

