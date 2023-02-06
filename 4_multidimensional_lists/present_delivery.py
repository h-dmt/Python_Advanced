# You will receive an integer m for the number of presents Santa has and an integer n
# for the size of the neighborhood with a square shape. On the following lines,
# you will receive the matrix, which represents the neighborhood.
# Santa will be in a random cell, marked with the letter "S".
# Each cell stands for a house where children may live. If the cell has "X" on it,
# that means there lives a naughty kid. Otherwise, if a nice kid lives there, the cell is marked by "V".
# There can also be cells marked with "C" for cookies. All of the empty positions will be marked with "-".
# Santa can move "up", "down", "left", "right" with one position each time.
# These will be the commands that you receive.
# If he moves to a house with a nice kid, the kid receives a present,
# but if Santa reaches a house with a naughty kid, he doesn't drop a present.
# If the command sends Santa to a cell marked with "C",
# Santa eats cookies and becomes happy and extra generous to all the kids around him*
# (meaning all of them will receive presents - it doesn't matter if naughty or nice).
# If Santa has been to a house, the cell becomes "-".
# Note: *around him means on his left, right, upwards, and downwards by one cell.
# In this case, Santa doesn't move to these cells, or if he does, he returns to the cell where the cookie was.
# If Santa runs out of presents or receives the command "Christmas morning", you should end the program.
# Keep in mind that you should check whether all the nice kids received presents.

n_presents = int(input())
rows = int(input())
N = [[n for n in input().split()] for _ in range(rows)]
# S - Santa position, X - naughty kid, V - good kid, C - Cookies
nice_kids = 0
nice_kids_left = 0
move = {
    'up': lambda x, y: [x - 1, y],
    'down': lambda x, y: [x + 1, y],
    'right': lambda x, y: [x, y + 1],
    'left': lambda x, y: [x, y - 1],
}

for row in range(rows):
    for column in range(rows):
        if N[row][column] == 'V':
            nice_kids += 1
        elif N[row][column] == 'S':
            S = [row, column]
nice_kids_left = nice_kids
command = input()
while command != "Christmas morning":
    new_r, new_c = move[command](S[0], S[1])  # New Santa position
    old_r, old_c = S  # old Santa position
    if 0 <= new_r <= rows - 1 and 0 <= new_c <= rows - 1:
        if N[new_r][new_c] == 'C':  # Santa founds cookie
            S = [new_r, new_c]
            N[new_r][new_c] = 'S'
            N[old_r][old_c] = '-'
            for direction in move:
                r_c, c_c = move[direction](new_r, new_c)
                if N[r_c][c_c] == 'V':
                    nice_kids_left -= 1
                    n_presents -= 1
                    N[r_c][c_c] = '-'
                elif N[r_c][c_c] == 'X':
                    n_presents -= 1
                    N[r_c][c_c] = '-'
        elif N[new_r][new_c] == 'V':  # Found a good kid
            S = [new_r, new_c]
            N[new_r][new_c] = 'S'
            N[old_r][old_c] = '-'
            nice_kids_left -= 1
            n_presents -= 1
        elif N[new_r][new_c] == 'X':  # Naughty kid
            S = [new_r, new_c]
            N[new_r][new_c] = 'S'
            N[old_r][old_c] = '-'
        elif N[new_r][new_c] == '-':  # Empty
            S = [new_r, new_c]
            N[new_r][new_c] = 'S'
            N[old_r][old_c] = '-'

    if n_presents == 0:
        if nice_kids_left:  # no present for the remaining good kids
            print("Santa ran out of presents!")
        break
    command = input()

[print(*n) for n in N]
if not nice_kids_left:
    print(f"Good job, Santa! {nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids_left} nice kid/s.")