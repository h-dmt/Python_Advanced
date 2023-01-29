# The knight game is played on a board with dimensions N x N.
# You will receive a board with "K" for knights and "0" for empty cells.
# Your task is to remove knights until no knights that can attack one another with one move are left.
# Always remove the knight who can attack the greatest number of knights.
# If there are two or more knights with the same number of attacks, remove the top-left one.
# Input
#     • On the first line, you will receive integer N - the size of the board
#     • On the following N lines, you will receive strings with "K" and "0"
# Output
#     • Print a single integer with the number of knights that need to be removed.

n = int(input())
B = [list(input()) for _ in range(n)]
k_moves = [(2, -1),
           (2, 1),
           (1, 2),
           (-1, 2),
           (-2, 1),
           (-2, -1),
           (-1, -2),
           (1, -2)
           ]
K_max_attacks = {}
removed_kings = 0
while True:
    for row in range(n):
        for col in range(n):
            if B[row][col] == 'K':
                if (row, col) not in K_max_attacks:
                    K_max_attacks[(row, col)] = 0
                # check movements
                for move in k_moves:
                    r, c = move
                    if 0 <= row + r <= n - 1 and 0 <= col + c <= n - 1:  # then move is valid
                        if B[row+r][col+c] == 'K':
                            if (row+r, col+c) not in K_max_attacks:
                                K_max_attacks[(row+r, col+c)] = 0
                            K_max_attacks[row, col] += 1
    K_max_sorted = dict(sorted(K_max_attacks.items(), key=lambda x: (-x[1], x[0])))
    # remove the knight who can attack the greatest number of knights.
    # If there are two or more knights with the same number of attacks, remove the top-left one.
    first_key = list(K_max_sorted.keys())[0]
    if K_max_sorted[first_key] != 0:
        K_max_sorted.pop(first_key)
        rr, cc = first_key
        B[rr][cc] = '0'
        removed_kings += 1
        K_max_attacks.clear()
        K_max_sorted.clear()
    else:
        break
print(removed_kings)
