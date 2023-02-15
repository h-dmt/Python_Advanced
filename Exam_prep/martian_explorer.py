# https://judge.softuni.org/Contests/Practice/Index/3430#1

SIZE = 6
deposits = {'W': 'Water',
            'M': 'Metal',
            'C': 'Concrete',
            'R': 'Rock'}
deposits_found = {'W': 0, 'M': 0, 'C': 0}
broken = False
rover = []
field = []
for r in range(SIZE):
    field_row = input().split()
    field.append(field_row)
    if 'E' in field_row:
        rover = [r, field_row.index('E')]

directions = {'up': lambda x, y: ((x - 1) % SIZE, y),
              'down': lambda x, y: ((x + 1) % SIZE, y),
              'right': lambda x, y: (x, (y + 1) % SIZE),
              'left': lambda x, y: (x, (y - 1) % SIZE)}

commands = input().split(', ')

for command in commands:

    field[rover[0]][rover[1]] = '-'
    row, col = directions[command](rover[0], rover[1])
    if field[row][col] == '-':
        rover = [row, col]
        field[row][col] = 'E'
        continue

    elif field[row][col] in deposits:
        deposit = field[row][col]

        if deposit != 'R':  # a deposit was found
            rover = [row, col]
            field[row][col] = 'E'
            print(f"{deposits[deposit]} deposit found at ({row}, {col})")
            deposits_found[deposit] += 1

        else:  # rover landed on rock and got broken
            rover = [row, col]
            print(f"Rover got broken at ({row}, {col})")
            break

if all(deposits_found.values()):
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")
