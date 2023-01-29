"""
Each robot has a processing time – it is the time in seconds the robot needs to process a product.
When a robot is free, it should take a product for processing and log its name, product, and processing
start time.
Each robot processes a product coming from the assembly line. A product is coming from the line each second
(so the first product should appear at [start time + 1 second]).
If a product passes the line and there is not a free robot to take it, it should be queued at the end of the
line again.
The robots are standing in the line in the order of their appearance.
Input
    • On the first line, you will receive the robots' names and their processing times in the format
    "robotName-processTime;robotName-processTime;robotName-processTime..."
    • On the second line, you will get the starting time in the format "hh:mm:ss"
    • Next, until the "End" command, you will get a product on each line.
Output
    • Every time a robot takes a product, you should print: "{robotName} - {product} [hh:mm:ss]
"""
from collections import deque
from datetime import datetime, timedelta

robot_lst = input().split(';')
products = deque()
robots = {r: [int(t), 0] for r, t in (robot.split('-') for robot in robot_lst)}
production_time = datetime.strptime(input(), "%H:%M:%S")
while True:
    product = input()
    if product == 'End':
        break
    products.append(product)
free_robot = []

while products:
    cur_product = products.popleft()
    production_time += timedelta(0, 1)  # a product arrives every sec
    free_robot = deque(r for r in robots if robots[r][1] <= 0)
    if free_robot:
        cur_robot = free_robot.popleft()
        robots[cur_robot][1] = robots[cur_robot][0]
        print(f"{cur_robot} - {cur_product} [{production_time.strftime('%H:%M:%S')}]")
    else:
        products.append(cur_product)
    for r in robots:
        robots[r][1] -= 1  # time ticking for every robot
