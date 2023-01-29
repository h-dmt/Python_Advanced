"""
reads lines of input consisting of a customer's name and adds it to the
end of a queue until "End" is received. If, in the meantime, you receive the command "Paid",
you should print each customer in the order they are served (from the first to the last one)
and empty the queue.
When you receive "End", you should print the count of the remaining people in the queue
in the format: "{count} people remaining."
"""

from collections import deque


def paid_clients(names):
    for name in names:
        print(name)


in_name = input()
name_queue = deque()
while in_name != 'End':
    if in_name == 'Paid':
        paid_clients(name_queue)
        name_queue.clear()
    else:
        name_queue.append(in_name)
    in_name = input()
count = len(name_queue)
print(f"{count} people remaining.")
