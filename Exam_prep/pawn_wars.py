"""
We will play the game with two pawns, white (w) and black (b), where they can:
    • Only move forward in a straight line:
            ▪ White (w) moves from the 1st rank to the 8th rank direction.
            ▪ Black (b) moves from 8th rank to the 1st rank direction.
    • Can move only 1 square at a time.
    • Can capture another pawn in from of them only diagonally:

Some rules apply when moving paws:
    • If the two pawns interact diagonally, the player, in turn, must capture the opponent's pawn.
    When a pawn captures another pawn, the game is over.
    • If no capture is possible, the pawns keep on moving until one of them reaches the last rank.

"""

rows = 8  # 8x8 Board
cols = {0: 'a',
        1: 'b',
        2: 'c',
        3: 'd',
        4: 'e',
        5: 'f',
        6: 'g',
        7: 'h'}


def move(color, pawn):  # moves the pawn around the board
    r_pawn, c_pawn = pawn

    if color == 'w':
        r_new, c_new = r_pawn - 1, c_pawn

    elif color == 'b':
        r_new, c_new = r_pawn + 1, c_pawn

    if 0 <= r_new < rows:  # validation of rows
        B[r_pawn][c_pawn] = '-'
        pawn = r_new, c_new
        B[r_new][c_new] = color
    # [print(*b) for b in B]
    # print()
    return pawn


def check_capture(color, pawn):
    p_r, p_c = pawn  # pawn position
    w_diagonals = {'wl': lambda r, c: [r - 1, c - 1],
                   'wr': lambda r, c: [r - 1, c + 1]}

    b_diagonals = {'bl': lambda r, c: [r + 1, c - 1],
                   'br': lambda r, c: [r + 1, c + 1]}

    if color == 'w':  # if white turn
        for direction in w_diagonals:
            rr, cc = w_diagonals[direction](p_r, p_c)
            if 0 <= rr < 7 and 0 <= cc < 7:
                if B[rr][cc] == 'b':
                    capture_position = w_diagonals[direction](p_r, p_c)
                    return capture_position

    if color == 'b':  # if black turn
        for direction in b_diagonals:
            rr, cc = b_diagonals[direction](p_r, p_c)
            if 0 <= rr < 7 and 0 <= cc < 7:
                if B[rr][cc] == 'w':
                    capture_position = b_diagonals[direction](p_r, p_c)
                    return capture_position
    return False


def play(color, pawn):

    capture = check_capture(color, pawn)  # check if a capture can be made
    if capture:
        cap_row, cap_col = capture
        cap_row = 7 - cap_row + 1
        cap_col = cols[cap_col]
        square = cap_col + str(cap_row)
        col = 'White' if color == 'w' else 'Black'
        print(f"Game over! {col} win, capture on {square}.")
        quit()

    else:  # if not move straight
        pawn = move(color, pawn)
        if color == 'w' and pawn[0] == 0:  # white reached end of board
            column = cols[pawn[1]]
            square = column + '8'
            print(f"Game over! White pawn is promoted to a queen at {square}.")
            quit()
        if color == 'b' and pawn[0] == 7:  # black reached end of board
            column = cols[pawn[1]]
            square = column + '1'
            print(f"Game over! Black pawn is promoted to a queen at {square}.")
            quit()
    return pawn


B = [[b for b in input().split()] for _ in range(rows)]  # creating the board
position = {'w': [7, 0], 'b': [0, 0]}

for r in range(rows):
    for c in range(rows):
        if B[r][c] == 'b':  # find black pawn
            position['b'] = [r, c]
        elif B[r][c] == 'w':  # find white pawn
            position['w'] = [r, c]
value = [0, 0]

while value != 'End':
    for color in ['w', 'b']:
        value = play(color, position[color])
        if value == 'End':
            break
        else:
            position[color] = value

# Example input:
"""
- - - - - - b -
- - - - - - - -
- - - - - - - -
- - - - - - - -
- - - - - - - -
- w - - - - - -
- - - - - - - -
- - - - - - - -
"""