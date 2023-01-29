"""
On the first line, you will receive the starting quantity of water (integer) in a dispenser. Then,
on the following lines, you will be given the names of some people who want to get water
(each on a separate line) until you receive the command "Start". Add those people in a
queue. Finally, you will receive some commands until the command "End":
    "{liters}" - litters (integer) that the current person in the queue wants to get. Check
    if there is enough water in the dispenser for that person.
        o If there is enough water, print "{person_name} got water" and remove
          him/her from the queue.
        o Otherwise, print "{person_name} must wait" and remove the person from
          the queue without reducing the water in the dispenser.
    "refill {liters}" - add the given litters in the dispenser.
In the end, print how many liters of water have left in the format: "{left_liters} liters
left".
"""
from collections import deque

current_quantity = int(input())
COMMAND_start = 'Start'
COMMAND_End = 'End'
users_que = deque()
command = input()
while command != COMMAND_start:
    users_que.append(command)
    command = input()
command = input()
while command != COMMAND_End:
    if command.startswith('refill'):
        refil = command.split(' ')
        current_quantity += int(refil[1])
    else:
        qty = int(command)
        if qty <= current_quantity:
            print(f"{users_que[0]} got water")
            current_quantity -= qty
            users_que.popleft()
        else:
            print(f"{users_que[0]} must wait")
            users_que.popleft()
    command = input()
print(f"{current_quantity} liters left")
