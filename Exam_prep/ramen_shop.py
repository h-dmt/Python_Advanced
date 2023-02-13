# You will be given two sequences of integers representing bowls of ramen and customers.
# Your task is to find out if you can serve all the customers.
# Start by taking the last bowl of ramen and the first customer.
# Try to serve every customer with ramen until we have no more ramen or customers left:
#     • Each time the value of the ramen is equal to the value of the customer, remove them both and continue with
#     the next bowl of ramen and the next customer.
#     • Each time the value of the ramen is bigger than the value of the customer, decrease the value of that ramen
#     with the value of that customer and remove the customer. Then try to match the same bowl of ramen
#     (which has been decreased) with the next customer.
#     • Each time the customer's value is bigger than the value of the ramen bowl,
#     decrease the value of the customer with the value of the ramen bowl and remove the bowl. T
#     hen try to match the same customer (which has been decreased) with the next bowl of ramen.
# Look at the examples provided for a better understanding of the problem.

from collections import deque

bowls = deque(list(map(int, input().split(', '))))
clients = deque(list(map(int, input().split(', '))))

while bowls and clients:
    bowl = bowls.pop()
    client = clients.popleft()
    if bowl > client:
        bowl -= client
        bowls.append(bowl)
    elif client > bowl:
        client -= bowl
        clients.appendleft(client)

if not clients:
    print("Great job! You served all the customers.")
    if bowls:
        bowls = list(map(str, bowls))
        print(f"Bowls of ramen left: {', '.join(bowls)}")

else:
    print("Out of ramen! You didn't manage to serve all customers.")
    if clients:
        clients = list(map(str, clients))
        print(f"Customers left: {', '.join(clients)}")

# Example input:

"""
30, 13, 45
70, 25, 55, 15
------------------
14, 25, 37, 43, 19
58, 23, 37
"""