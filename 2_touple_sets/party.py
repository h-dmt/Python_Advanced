"""
On the first line, you will receive the number of guests – N.
On the following N lines, you will be receiving their reservation codes.
All reservation codes are 8 characters long, and all VIP numbers will start with a digit.
    § Keep in mind that all reservation numbers must be unique.
    § When a guest comes, check if they exist on any of the two reservation lists.

After that, you will be receiving guests who came to the party until you read the "END" command.
In the end, print the number of guests who did not come to the party and their reservation numbers:
    • The VIP guests must be first.
    • Both the VIP and the Regular guests must be sorted in ascending order.
"""

reservation = {input() for _ in range(int(input()))}
attending = set()
guest = input()
while guest != 'END':
    if guest in reservation:
        attending.add(guest)
    guest = input()

not_attending = reservation - attending
print(len(not_attending))
print(*sorted(not_attending), sep='\n')
