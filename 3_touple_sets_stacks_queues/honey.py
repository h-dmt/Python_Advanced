##############################################################################################################
# You will receive 3 sequences:                                                                              #
#     • a sequence of integers, representing working bees                                                    #
#     • a sequence of integers, representing nectar                                                          #
#     • a sequence of symbols – "+", "-", "*" or "/", representing the honey-making process.                 #
# Your task is to check if the bee has collected enough nectar to return to the hive and keep track of the   #
# total honey waiting bees made with the collected nectar.                                                   #
# Step one: check if a bee has collected enough nectar. You should take the first bee and try to match it    #
# with the last nectar:                                                                                      #
#     • If the nectar value is more or equal to the value of the bee, it is considered collected,            #
#     and the bee returns to the hive to drop off the load (step two).                                       #
#     • If the nectar value is less than the value of the bee, you should remove the nectar and try to match #
#     the bee with the next nectar's value until the bee collects enough nectar.                             #
# Step two: When a bee successfully collects nectar, she returns to the hive, and you should calculate the   #
# honey made. Take the first symbol in the sequence of symbols ("+", "-", "*" or "/") and make the           #
# corresponding calculation:                                                                                 #
#   "{matched_bee} {symbol} {matched_nectar}"                                                                #
#                                                                                                            #
# The result represents the honey that is made from the passed nectar.                                       #
# The calculation should always return the absolute value of the result. After the calculation,              #
# remove the bee, the nectar, and the symbol.                                                                #
# Stop making honey when you are out of bees or nectar.                                                      #
##############################################################################################################

from collections import deque

working_bees = deque(int(b) for b in input().split())
nectar_que = deque(int(n) for n in input().split())
operations_deq = deque(o for o in input().split())
collected_nectar = deque()
total_honey = 0
operations_func = {
    '+': lambda x, y: x+y,
    '-': lambda x, y: abs(x-y),
    '*': lambda x, y: x*y,
    '/': lambda x, y: x/y,
}
# Collecting process
while working_bees and nectar_que:
    #  if nectar value >= bee value collect it
    if nectar_que[-1] >= working_bees[0]:
        if nectar_que[-1] == 0 and working_bees[0] == 0:  # remove also the bee????
            working_bees.popleft()
            nectar_que.pop()
            continue
        collected_nectar.append([working_bees.popleft(), nectar_que.pop(), operations_deq.popleft()])
    #  else remove nectar value
    else:
        nectar_que.pop()
        continue

# Making process
while collected_nectar:
    bee, nectar, op_symb = collected_nectar.popleft()
    total_honey += operations_func[op_symb](bee, nectar)

print(f"Total honey made: {total_honey}")
if working_bees:
    bees_left = list(map(str, working_bees))
    print(f"Bees left: {', '.join(bees_left)}")
if nectar_que:
    nectar_left = list(map(str, nectar_que))
    print(f"Nectar left: {', '.join(nectar_left)}")
