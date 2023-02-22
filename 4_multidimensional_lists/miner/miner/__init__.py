def create_field(size):
    field = []
    coal = 0
    position = ()
    for r in range(size):
        row = input().split()
        field.append(row)
        for col in range(size):
            if field[r][col] == 'c':
                coal += 1
            elif field[r][col] == 's':
                position = (r, col)

    return field, coal, position


def move(direct, field, coal, position, directions):
    r, c = directions[direct](*position)
    size = len(field)
    if 0 <= r < size and 0 <= c < size:
        field[position[0]][position[1]] = '*'

        if field[r][c] == '*':
            field[r][c] = 's'
            position = (r, c)

        elif field[r][c] == 'c':
            coal -= 1
            field[r][c] = 's'
            position = (r, c)
            if coal == 0:
                print(f"You collected all coal! ({r}, {c})")
                return True, field, coal, position

        elif field[r][c] == 'e':
            field[r][c] = 's'
            position = (r, c)
            print(f"Game over! ({r}, {c})")
            return True,  field, coal, position

    return False, field, coal, position
