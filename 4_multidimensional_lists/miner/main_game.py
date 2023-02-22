"""
First, you will receive the size of a square field in which the miner should move.
On the second line, you will receive the commands for the miner's movement, separated by a single space.
The possible commands are "left", "right", "up" and "down".
In the end, you will receive each row of the field on a separate line. The possible characters that may
appear on the screen are:
    • * - a regular position on the field
    • e - the end of the route
    • c - coal
    • s - miner
The miner starts moving from the position "s". He should perform the given commands successively,
moving with only one position in the given direction. If the miner has reached the edge of the field and
the following command indicates that he has to get out of the area, he must remain in his current position
and ignore the command.
When the miner finds coal, he collects it and replaces it with "*". Keep track of the collected coal.
In the end, you should print whether the miner has succeeded in collecting the coal or not and his final position:
    • If the miner has collected all coal in the field, the program stops, and you should print
    the message: "You collected all coal! ({row_index}, {col_index})".
    • If the miner steps at "e", the game is over (the program stops), and you should print the message:
     "Game over! ({row_index}, {col_index})".
    • If there are no more commands and none of the above cases had happened, you should print the message:
    "{number_of_remaining_coal} pieces of coal left. ({row_index}, {col_index})".
"""
from collections import deque
from miner import *

SIZE = int(input())  # size of the square field
commands = deque(input().split())  # directions separated by space

directions = {'up': lambda x, y: (x - 1, y),
              'down': lambda x, y: (x + 1, y),
              'right': lambda x, y: (x, y + 1),
              'left': lambda x, y: (x, y - 1)}


end_game = False
field, coal, position = create_field(SIZE)
while commands:
    command = commands.popleft()
    end_game, field, coal, position = move(command, field, coal, position, directions)

if not end_game:
    print(f"{coal} pieces of coal left. ({position[0]}, {position[1]})")


"""
Example input:

6
left left down right up left left down down down
* * * * * *
e * * * c *
* * c s * *
* * * * * *
c * * * c *
* * c * * *
"""