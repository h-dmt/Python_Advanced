"""
Write a program that:
    • Records a car number for every car that enters the parking lot
    • Removes a car number when the car leaves the parking lot
On the first line, you will receive the number of commands - N. On the following N lines,
you will receive the direction and car's number in the format: "{direction}, {car_number}".
The direction could only be "IN" or "OUT". Print the car numbers which are still in the parking lot.
Keep in mind that all car numbers must be unique. If the parking lot is empty, print "Parking Lot is Empty".
"""
from collections import deque

car_in = deque()
for _ in range(int(input())):
    in_out, plate = input().split(', ')
    if in_out == 'IN' and plate not in car_in:
        car_in.append(plate)
    elif in_out == 'OUT' and plate in car_in:
        car_in.remove(plate)
if car_in:
    print(*car_in, sep='\n')
else:
    print("Parking Lot is Empty")
