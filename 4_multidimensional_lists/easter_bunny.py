#     • One bunny - randomly placed in it and marked with the symbol "B"
#     • Number of eggs placed at different positions of the field and traps marked with "X"
# Your job is to determine the direction in which the bunny should go to collect the maximum number of eggs.
# The directions that should be considered as possible are up, down, left, and right.
# If you reach a trap while checking some of the directions,
# you should not consider the fields after the trap in this direction.
#
# Note: Consider ONLY the paths from which the bunny has collected 1 or more eggs.
# Input
#     • A number representing the size of the field
#     • The matrix representing the field (each position separated by a single space)
# Output
#     • The direction which should be considered as best (lowercase)
#     • The field positions from which we are collecting eggs as lists
#     • The total number of eggs collected

rows = int(input())
F = [[int(f) if f.lstrip('-').isnumeric() else str(f) for f in input().split()] for _ in range(rows)]

directions = {'up': lambda r, c: [r - 1, c],
              'down': lambda r, c: [r + 1, c],
              'right': lambda r, c: [r, c + 1],
              'left': lambda r, c: [r, c - 1],
              }


def check_directions(bunny, dirr):
    eggs = 0
    moves = []
    while 0 <= directions[dirr](*bunny)[0] <= rows - 1 and 0 <= directions[dirr](*bunny)[1] <= rows - 1:
        r, c = directions[dirr](*bunny)  # jump to new position
        bunny = [r, c]  # update bunny position
        if F[r][c] == 'X':
            break
        else:
            eggs += F[r][c]
            moves.append([r, c])
    return eggs, moves


move = {}
collected_eggs = 0
max_collected_eggs = 0
best_move = {}
B = []
for row in range(rows):
    for col in range(rows):
        if F[row][col] == 'B':
            B = [row, col]
for direction in directions:
    collected_eggs, move = check_directions(B, direction)  # passing the matrix and which direction
    if collected_eggs >= max_collected_eggs and move:
        max_collected_eggs = collected_eggs
        best_move = {direction: move}
    else:
        move = []
for k in best_move:
    print(k)
    print(*best_move[k], sep='\n')
print(max_collected_eggs)
