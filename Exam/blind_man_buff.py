
N_rows, M_cols = [int(n) for n in input().split()]

field = []
position = (0, 0)
opponents_count = 0
for row in range(N_rows):
    field_row = input().split()
    field.append(field_row)
    for el in field_row:
        if el == 'B':
            position = (row, field_row.index('B'))
        elif el == 'P':
            opponents_count += 1

touch_count = 0
movements = 0

directions = {'up': lambda x, y: (x - 1, y),
              'down': lambda x, y: (x + 1, y),
              'right': lambda x, y: (x, y + 1),
              'left': lambda x, y: (x, y - 1)}


def validate_move(dir):
    global position, field
    r, c = directions[dir](*position)
    if 0 <= r < N_rows and 0 <= c < M_cols:  # check inside the field
        if field[r][c] != 'O':
            return r, c
    else:
        return False


command = input()
while command != 'Finish':

    if validate_move(command):
        r, c = validate_move(command)
        field[position[0]][position[1]] = '-'

        if field[r][c] == 'P':
            touch_count += 1
            opponents_count -= 1
        movements += 1
        position = (r, c)
        field[r][c] = 'B'
    if opponents_count == 0:
        break
    else:
        command = input()

print("Game over!")
print(f"Touched opponents: {touch_count} Moves made: {movements}")
