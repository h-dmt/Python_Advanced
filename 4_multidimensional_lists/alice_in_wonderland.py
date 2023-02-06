# Alice is going to the mad tea party, to see her friends. On the way to the party,
# she needs to collect bags of tea.
# You will be given an integer n for the size of the Wonderland territory with a square shape.
# On the following n lines, you will receive the rows of the territory:
#     • Alice will be placed in a random position, marked with the letter "A".
#     • On the territory, there will be bags of tea, represented as numbers.

#     If Alice steps on a number position, she collects the tea bags and increases the quantity
#     with the corresponding number.
#     • There will always be one rabbit hole on the territory marked with the letter "R".
#     • All of the empty positions will be marked with ".".
# After the field state, you will be given commands for Alice's movements.
# Move commands can be: "up", "down", "left" or "right".
# When Alice collects at least 10 bags of tea, she is ready to go to the tea party,
# and she does not need to continue collecting.
# Otherwise, if she steps on the rabbit hole or goes out of the territory, she can't return,
# and the program ends.
# In the end, the path she walked had to be marked with '*'.

n = int(input())
M = [[int(m) if m.isnumeric() else str(m) for m in input().split()] for _ in range(n)]
A = (0, 0)
directions = {
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c),
    'left': lambda r, c: (r, c - 1),
    'right': lambda r, c: (r, c + 1),
}
tea_bags = 0
Rabbit_hole = False
for row in range(n):
    for col in range(n):
        if M[row][col] == 'A':
            A = (row, col)
            M[row][col] = '*'

            while tea_bags < 10 and not Rabbit_hole:
                command = input()
                step_r, step_c = directions[command](A[0], A[1])  # Passing Alice position to the lambda func
                if 0 <= step_r <= n - 1 and 0 <= step_c <= n - 1:  # Check new position is valid
                    A = (step_r, step_c)
                    if M[step_r][step_c] == 'R':
                        M[step_r][step_c] = '*'
                        Rabbit_hole = True
                    elif M[step_r][step_c] == '.':
                        M[step_r][step_c] = '*'
                    elif M[step_r][step_c] == '*':
                        continue
                    else:
                        tea_bags += M[step_r][step_c]  # found tea bags
                        M[step_r][step_c] = '*'
                else:
                    break

if tea_bags >= 10 and not Rabbit_hole:
    print("She did it! She went to the party.")
    [print(*m) for m in M]
else:
    print("Alice didn't make it to the tea party.")
    [print(*m) for m in M]
