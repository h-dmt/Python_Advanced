# https://judge.softuni.org/Contests/Practice/Index/3744#1

SIZE = int(input())
battlefield = []
submarine = [0, 0]
damage = 0
cruisers = 3
disappeared = False

for r in range(SIZE):
    row = list(input())
    battlefield.append(row)
    if 'S' in row:
        submarine = [r, row.index('S')]
        battlefield[r][row.index('S')] = '-'

directions = {
    'up': lambda x, y: ((x - 1) % SIZE, y),
    'down': lambda x, y: ((x + 1) % SIZE, y),
    'right': lambda x, y: (x, (y + 1) % SIZE),
    'left': lambda x, y: (x, (y - 1) % SIZE),
}


def navigate(direct):
    global submarine, damage, cruisers, disappeared, battlefield
    r, c = directions[direct](submarine[0], submarine[1])
    battlefield[submarine[0]][submarine[1]] = '-'

    if battlefield[r][c] == '*':  # we have hit a mine
        damage += 1
        if damage == 3:  # submarine is sunk and disappears
            disappeared = [r, c]
            # report last coordinate
            print(f"Mission failed, U-9 disappeared! Last known coordinates [{r}, {c}]!")
    if battlefield[r][c] == 'C':
        cruisers -= 1  # a cruiser is sunk
    battlefield[r][c] = 'S'
    submarine = [r, c]
    return cruisers, disappeared


while cruisers and not disappeared:

    command = input()
    cruisers, disappeared = navigate(command)

# Print the output
if not cruisers:
    print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
for row in battlefield:
    print(''.join(row))

# Example input:
"""
5
*--*-
-S-*C
-*---
-----
-C-*C
right
down
left
up
right
right
right
down
down
down
up
left
left
left
down
"""