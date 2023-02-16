# https://judge.softuni.org/Contests/Practice/Index/2812#1

from math import floor

SIZE = int(input())
coins = 0
position = (0, 0)
field = []
path = []
# creating the field
for row in range(SIZE):
    field_row = input().split()
    field.append(field_row)
    if 'P' in field_row:
        position = (row, field_row.index('P'))

# directions with lambda functions
directions = {'up': lambda x, y: ((x - 1) % SIZE, y),
              'down': lambda x, y: ((x + 1) % SIZE, y),
              'right': lambda x, y: (x, (y + 1) % SIZE),
              'left': lambda x, y: (x, (y - 1) % SIZE)}

while coins < 100:
    command = input()
    old_r, old_c = position[:]
    path.append([old_r, old_c])
    r, c = directions[command](*position)
    field[old_r][old_c] = 0

    if field[r][c] == 'X':  # hit a wall and break
        coins = floor(coins / 2)
        path.append([r, c])
        print(f"Game over! You've collected {coins} coins.")
        break

    elif field[r][c] != 'X':
        coins += int(field[r][c])
        position = (r, c)
        if coins >= 100:
            path.append([r, c])
            print(f"You won! You've collected {coins} coins.")
            break

print("Your path:")
print(*path, sep='\n')

