"""
Write a program that reads a rectangular matrix's dimensions and finds the 3x3 square with a maximum
sum of its elements. There will be no case with two or more 3x3 squares with equal maximal sum.

Input
    • On the first line, you will receive the rows and columns in the format "{rows} {columns}" – integers in the range [1, 20]
    • On the following lines, you will receive each row with its columns - integers, separated by a single space in the range [-20, 20]
"""


r, c = [int(x) for x in input().split()]
matrix = [[int(x) for x in input().split()] for _ in range(r)]

max_sum = float("-inf")
biggest_matrix = []

for row in range(r - 2):
    for col in range(c -2):
        first_row = matrix[row][col:col+3]
        second_row = matrix[row + 1][col:col + 3]
        third_row = matrix[row + 2][col:col + 3]

        current_sum = sum(first_row) + sum(second_row) + sum(third_row)
        if current_sum > max_sum:
            max_sum = current_sum
            biggest_matrix = [first_row, second_row, third_row]
print(f"Sum = {max_sum}")
[print(*biggest_matrix[row]) for row in range(3)]
