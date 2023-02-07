# You will be given a matrix with 5 rows and 5 columns. It is a shotgun range represented
# as some symbols separated by a single space:
#     • Your position is marked with the symbol "A"
#     • Targets marked with symbol "x"
#     • All of the empty positions will be marked with "."
# After the field state, you will be given an integer representing the number of commands you will receive.
# The possible commands are:
#     • "move {right/left/up/down} {steps}" – you should move in the given direction with the given steps.
#     You can only move if the field you want to step on is marked with ".".
#     • "shoot {right/left/up/down}" – you should shoot in the given direction
#     (from your current position without moving). Beware that there might be targets that stand
#     in the way of other targets, and you cannot reach them - you can shoot only the nearest target.
#     When you have shot a target, the field becomes empty position (".").
# Validate the positions since they can be outside the field.
# Keep track of all the shot targets:
#     • If at any point there are no targets left, end the program and print:
#     "Training completed! All {count_targets} targets hit.".
#     • If, after you perform all the commands, there are some targets left print:
#     "Training not completed! {count_left_targets} targets left.".


def valid_direction(row, col):
    size = 5
    if 0 <= row <= size - 1 and 0 <= col <= size - 1:
        return True
    else:
        return False


def next_position(heading, cur_row, cur_col):
    directions = {
        'up': lambda r, c: [r - 1, c],
        'down': lambda r, c: [r + 1, c],
        'left': lambda r, c: [r, c - 1],
        'right': lambda r, c: [r, c + 1],
    }
    new_r, new_c = directions[heading](cur_row, cur_col)
    return [new_r, new_c]


class Shooter:
    def __init__(self, rows=5):
        self.rows = rows
        self.n_targets = 0
        self.targets_left = 0
        self.targets_shot = []
        self_A = []
        self.M = []
        self.make_matrix()

    def make_matrix(self, ):

        for _ in range(self.rows):  # create matrix rows x rows
            self.M.append(input().split())
        # print(self.M)

        for row in range(self.rows):  # find initial position and count targets
            for col in range(self.rows):
                if self.M[row][col] == 'A':
                    self.A = [row, col]
                elif self.M[row][col] == 'x':
                    self.n_targets += 1
        self.targets_left = self.n_targets

    def shoot(self, direction):
        row_A, col_A = self.A
        r_next, c_next = next_position(direction, row_A, col_A)
        while True:

            if valid_direction(r_next, c_next):
                if self.M[r_next][c_next] == 'x':
                    self.targets_shot.append([r_next, c_next])
                    self.targets_left -= 1
                    self.M[r_next][c_next] = '.'
                    break  # target shot

            else:  # out of the field
                break

            r_next, c_next = next_position(direction, r_next, c_next)

    def move(self, direction, count):
        row_A, col_A = self.A
        for step in range(count):
            r_next, c_next = next_position(direction, row_A, col_A)
            if valid_direction(r_next, c_next):  # check if inside the field
                if self.M[r_next][c_next] == '.':  # Move only if marked with '.' !
                    self.M[self.A[0]][self.A[1]] = '.'
                    self.A = [r_next, c_next]
                    self.M[r_next][c_next] = 'A'
                    row_A, col_A = self.A
                elif self.M[r_next][c_next] == 'x':  # if a target is encountered just pass through it
                    row_A, col_A = r_next, c_next    # without occupying it's place
            else:
                break

            #[print(*m) for m in self.M]

    def __repr__(self):
        if self.targets_left == 0:
            return f"Training completed! All {self.n_targets} targets hit."
        else:
            return f"Training not completed! {self.targets_left} targets left."


shooter = Shooter()
n = int(input())
for _ in range(n):
    command = input().split()
    if command[0] == 'shoot':
        direct = command[1]
        shooter.shoot(direct)
        if shooter.targets_left == 0:
            break
    elif command[0] == 'move':
        direct = command[1]
        steps = int(command[2])
        shooter.move(direct, steps)

print(shooter)
for target in shooter.targets_shot:
    print(target)
