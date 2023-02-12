#  https://judge.softuni.org/Contests/Practice/Index/3596#1

size = int(input())
car = input()
T = [[t for t in input().split()] for _ in range(size)]  # Track
# [print(*t) for t in T]
finish = False
car_position = [0, 0]
T[0][0] = 'C'
distance = 0
directions = {'left': lambda x, y: [x, y - 1],
              'right': lambda x, y: [x, y + 1],
              'down': lambda x, y: [x + 1, y],
              'up': lambda x, y: [x - 1, y],
              }


def tunnel():
    global T, car_position, distance
    current_row, current_col = car_position
    for row in range(size):
        for col in range(size):
            if T[row][col] == 'T':  # car exits the tunnel here
                T[current_row][current_col] = '.'
                car_position = [row, col]
                T[row][col] = 'C'
                distance += 30
                break


def play(drive_dir):
    global T, car_position, distance

    current_row, current_col = car_position
    nex_row, next_col = directions[drive_dir](car_position[0], car_position[1])

    if 0 <= nex_row < size and 0 <= next_col < size:  # index validation

        if T[nex_row][next_col] == 'F':  # Final
            T[nex_row][next_col] = 'C'
            T[current_row][current_col] = '.'
            distance += 10
            return True

        elif T[nex_row][next_col] == 'T':  # car enters a tunnel
            T[nex_row][next_col] = 'C'
            T[current_row][current_col] = '.'
            car_position = [nex_row, next_col]
            tunnel()  # out of the tunnel

        else:
            car_position = [nex_row, next_col]  # Keep driving
            T[nex_row][next_col] = 'C'
            T[current_row][current_col] = '.'
            distance += 10
    return False


command = input()
while command != 'End' and not finish:

    finish = play(command)
    command = input()

if not finish:
    print(f"Racing car {car} DNF.")
else:
    print(f"Racing car {car} finished the stage!")
print(f"Distance covered {distance} km.")
[print(''.join(t)) for t in T]


# Example input:
"""
5
01
. . . . .
. . . T .
. . . . .
. T . . .
. . F . .
down
right
right
right
down
right
up
down
right
up
End
"""