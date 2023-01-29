"""
Your program should receive commands in the format: "swap {row1} {col1} {row2} {col2}"
where ("row1", "col1") and ("row2", "col2") are the coordinates of two points in the matrix.
A valid command starts with the "swap" keyword along with four valid coordinates
(no more, no less), separated by a single space.
    • If the command is valid, you should swap the values at the given indexes and print the
    matrix at each step (thus, you will be able to check if the operation was performed
    correctly).
    • If the command is not valid (does not contain the keyword "swap", has fewer or more
    coordinates entered, or the given coordinates are not valid), print "Invalid input!" and
    move on to the following command. A negative value makes the coordinates not valid.
Your program should finish when the command "END" is entered.
"""


def swap_element(the_matrix, r1, c1, r2, c2):
    el = the_matrix[r2][c2]
    the_matrix[r2][c2] = the_matrix[r1][c1]
    the_matrix[r1][c1] = el
    return the_matrix


rows, columns = [int(x) for x in input().split()]
Matrix = [[m for m in input().split()] for _ in range(rows)]

valid_row = range(rows)
valid_col = range(columns)

while True:
    command = input().split()
    if command[0] == 'swap':
        r1, c1 = [int(i) if i.isnumeric() else -1 for i in command[1:3]]
        r2, c2 = [int(i) if i.isnumeric() else -1 for i in command[3:5]]

        if {r1, r2}.issubset(valid_row) \
            and {c1, c2}.issubset(valid_col)\
                and len(command) == 5:  # Check if swap indexes are valid and number of elements

            Matrix = swap_element(Matrix, r1, c1, r2, c2)
            [print(*r) for r in Matrix]
        else:
            print('Invalid input!')
    elif command[0] == 'END':
        break
    else:
        print('Invalid input!')
