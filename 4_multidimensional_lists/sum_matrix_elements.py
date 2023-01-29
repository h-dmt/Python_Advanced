"""
Write a program that reads a matrix from the console and prints:
    • The sum of all numbers in the matrix
    • The matrix itself
On the first line, you will receive the matrix sizes in the format "{rows}, {columns}".
On the next rows, you will get elements for each column separated by a comma and a space ", ".
"""

rows, columns = list(map(int, input().split(', ')))
sum_M = 0
M = [[a for a in list(map(int, input().split(', ')))] for _ in range(rows)]

for r in range(rows):
    sum_M += sum(M[r])
print(sum_M)
print(M)
