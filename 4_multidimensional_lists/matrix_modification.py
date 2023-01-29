# Write a program that reads a matrix from the console and changes its values. On the first line,
# you will get the matrix's rows - N. You will get elements for each column on the following N lines,
# separated with a single space. You will be receiving commands in the following format:
#     • "Add {row} {col} {value}" – Increase the number at the given coordinates with the value.
#     • "Subtract {row} {col} {value}" – Decrease the number at the given coordinates by the value.
# If the coordinate is invalid, you should print "Invalid coordinates".
# A coordinate is valid if both of the given indexes are in range [0; len() – 1].
# When you receive "END", you should print the matrix and stop the program.

M = [[int(x) for x in input().split()] for _ in range(int(input()))]
operations = {'Add': lambda x, y: x + y,
              'Subtract': lambda x, y: x - y,
              }
while True:
    command = input().split()
    if command[0] == 'END':
        break
    else:
        operator, row, col, value = command
        row = int(row)
        col = int(col)
        value = int(value)
        if 0 <= row <= len(M) - 1 and 0 <= col <= len(M) - 1:
            x = M[row][col]
            M[row][col] = operations[operator](x, value)
        else:
            print("Invalid coordinates")

[print(*m) for m in M]
