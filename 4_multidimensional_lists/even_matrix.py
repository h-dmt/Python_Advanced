"""
Write a program that receives a matrix of numbers and prints a new one only with the numbers that are even.
Use nested comprehension for that problem.
On the first line, you will receive the rows of the matrix. On the next rows, y
ou will get elements for each column separated with a comma and a space ", ".
"""

M = [[j for j in list(map(int, input().split(', '))) if j % 2 == 0] for _ in range(int(input()))]

print(M)
