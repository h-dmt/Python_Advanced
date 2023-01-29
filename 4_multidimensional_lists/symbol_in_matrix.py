"""
Write a program that reads a number - N, representing the rows and columns of a square matrix.
On the next N lines, you will receive rows of the matrix. Each row consists of ASCII characters.
After that, you will receive a symbol. Find the first occurrence of that symbol in the matrix and
print its position in the format: "({row}, {col})". You should start searching from the top left.
If there is no such symbol, print the message "{symbol} does not occur in the matrix".
"""

n = int(input())
M = [[m for m in input()] for _ in range(n)]
the_symbol = input()
found = False
for r, row in enumerate(M):
    for c, element in enumerate(row):
        if element == the_symbol:
            print(f"({r}, {c})")
            found = True
            break
    if found:
        break
if not found:
    print(f"{the_symbol} does not occur in the matrix")
