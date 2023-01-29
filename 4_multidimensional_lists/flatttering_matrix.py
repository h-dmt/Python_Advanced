"""
Write a program that receives a matrix and prints the flattened version of it
(a list with all the values)
"""

M = [[m for m in list(map(int, input().split(', ')))] for _ in range(int(input()))]

M_flat = [x for row in M for x in row]
print(M_flat)
