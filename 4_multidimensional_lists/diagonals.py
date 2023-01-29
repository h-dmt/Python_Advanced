"""
Using a nested list comprehension, write a program that reads rows of a square matrix and its elements,
separated by a comma and a space ", ". You should find the matrix's diagonals, prints them and their sum
in the format:
"Primary diagonal: {element1}, {element2}, … {elementN}. Sum: {sum_of_primary}
Secondary diagonal: {element1}, {element2}, … {elementN}. Sum: {sum_of_secondary}".
"""

M = [[n for n in list(map(int, input().split(', ')))] for _ in range(int(input()))]
diag = [M[i][i] for i in range(len(M))]
diag_secondary = [M[len(M) - 1 - i][i] for i in range(len(M) - 1, -1, -1)]
print(f"Primary diagonal: {', '.join(str(n) for n in diag)}. Sum: {sum(diag)}")
print(f"Secondary diagonal: {', '.join(str(n) for n in diag_secondary)}. Sum: {sum(diag_secondary)}")
