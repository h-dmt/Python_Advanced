"""
Write a program that finds the difference between the sums of the square matrix diagonals (absolute value).
On the first line, you will receive an integer N - the size of a square matrix. T
he following N lines hold the values for each column - N numbers separated by a single space.
Print the absolute difference between the primary and the secondary diagonal sums.
"""

size = int(input())
M= [[i for i in list(map(int, input().split(' ')))] for _ in range(size)]
diag_1 = [M[i][i] for i in range(len(M))]
diag_2 = [M[len(M) - 1 - i][i] for i in range(len(M) - 1, -1, -1)]

print(abs(sum(diag_1) - sum(diag_2)))
