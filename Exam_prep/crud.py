# https://judge.softuni.org/Contests/Practice/Index/3534#1

SIZE = 6
table = [[t for t in input().split()] for _ in range(SIZE)]
position = input()
position = (int(position[1]), int(position[-2]))
directions = {'up': lambda x, y: (x - 1, y),
              'down': lambda x, y: (x + 1, y),
              'right': lambda x, y: (x, y + 1),
              'left': lambda x, y: (x, y - 1)}


def create(move, el):
    global table, position, SIZE
    r, c = directions[move](*position)
    if 0 <= r < SIZE and 0 <= c < SIZE:
        position = (r, c)
        if table[r][c] == '.':
            table[r][c] = el


def update(move, el):
    global table, position, SIZE
    r, c = directions[move](*position)
    if 0 <= r < SIZE and 0 <= c < SIZE:
        position = (r, c)
        if table[r][c] != '.':
            table[r][c] = el


def delete(move):
    global table, position, SIZE
    r, c = directions[move](*position)
    if 0 <= r < SIZE and 0 <= c < SIZE:
        position = (r, c)
        if table[r][c] != '.':
            table[r][c] = '.'


def read(move):
    global table, position, SIZE
    r, c = directions[move](*position)
    if 0 <= r < SIZE and 0 <= c < SIZE:
        position = (r, c)
        if table[r][c] != '.':
            print(f"{table[r][c]}")


command = input().split(', ')
while command[0] != 'Stop':

    if command[0] == 'Create':
        direction, value = command[1:]
        create(direction, value)

    elif command[0] == 'Update':
        direction, value = command[1:]
        update(direction, value)

    elif command[0] == 'Read':
        read(command[1])

    elif command[0] == 'Delete':
        delete(command[1])

    command = input().split(', ')

[print(*t) for t in table]

# Example input:
"""
H 8 . . . .
70 i . . . .
t . . . B .
50 . 16 . C .
. . . t . .
. 25 . . . .
(0, 0)
Read, right
Read, down
Read, left
Delete, down
Create, right, 10
Read, left
Stop
"""