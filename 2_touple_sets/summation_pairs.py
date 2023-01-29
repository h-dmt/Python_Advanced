"""
On the first line, you will receive a sequence of numbers separated by space. On the second line,
you'll receive a target number. Your task is to find the pairs of numbers whose sum equals the target number.
For each found pair print "{number} + {number} = {target_number}".
You may NOT use the same element twice to fulfill the condition above.
"""
from collections import deque

numbers = deque(map(int, input().split()))
target_sum = int(input())
while numbers:
    n1 = numbers.popleft()
    for n2 in numbers.copy():
        if n1 + n2 == target_sum:
            print(f"{n1} + {n2} = {target_sum}")
            numbers.remove(n2)
            break
