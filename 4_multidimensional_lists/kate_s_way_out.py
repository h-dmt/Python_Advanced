"""
Judge: https://judge.softuni.org/Contests/Practice/Index/1732#2

On the first line, you will be given how many rows there are in the maze. On the following n lines,
you will be given the maze itself. Here is a legend for the maze:
    • "#" - means a wall; Kate cannot go through there
    • " " - means empty space; Kate can go through there
    • "k" - the initial position of Kate; start looking for a way out from there
"""


def kate_got_out(r, c, F):
    # check if NOT inside the field
    if not (0 <= r < len(F)) or not (0 <= c < len(F[0])):
        return True
    return False


def set_of_directions(way, r, c):
    directions = {"u": lambda x, y: (x - 1, y),
                  "d": lambda x, y: (x + 1, y),
                  "r": lambda x, y: (x, y + 1),
                  "l": lambda x, y: (x, y - 1)}

    return directions[way](r, c)


def not_inside_field(row, col, field):
    if row < 0 or row >= len(field) or col < 0 or col >= len(field[0]):
        return True
    return False


def find_longest_path_out(paths_list):
    longest = []
    # print(paths_list)
    for p in paths_list:
        if len(longest) < len(p):
            longest = p
    # print(longest)
    return len(longest)


class KateWayOut:
    def __init__(self, rows):
        self.rows = rows
        self.field = []
        self.kate_pos = (0, 0)

    def create_field(self):

        for r in range(self.rows):
            self.field.append(list(input()))
            if 'k' in self.field[r]:
                self.kate_pos = (r, self.field[r].index('k'))

    def find_way_out(self, row, col, field, steps, ways_out):

        # base cases
        if kate_got_out(row, col, field):
            ways_out.append(steps)
            return

        if not_inside_field(row, col, field) or field[row][col] == "#" or field[row][col] == "|":
            return

        field[row][col] = '|'
        directions = ("u", "d", "r", "l")

        # backtracking
        for dirs in directions:
            new_row, new_col = set_of_directions(dirs, row, col)
            self.find_way_out(new_row, new_col, field, steps + [dirs], ways_out)

        # post action
        field[row][col] = ' '

        return ways_out

    def __str__(self):
        r, c = self.kate_pos
        paths_out = self.find_way_out(r, c, self.field, [], [])
        if paths_out:
            moves = find_longest_path_out(paths_out)

            return f"Kate got out in {moves} moves"

        return "Kate cannot get out"


kate_lab = KateWayOut(int(input()))
kate_lab.create_field()
print(kate_lab)


"""
Example input:
-------------

5
#########k 
##  #######
## #####  #
         ##
## ##### ##
-----------------------------
5
######
##  k#
## ###
######
## ###

Expected output:
Kate cannot get out
------------------------------
5
######### #
##  #####k#
## #####  #
         ##
## ##### ##

Expected output:
Kate got out in 12 moves
-----------------------------
4
######
##  k#
## ###
## ###
expected output:
Kate got out in 5 moves
"""
