"""
ou will be given three types of parentheses: (), {}, and [].
{[()]} - Parentheses are balanced.
(){}[] - Parentheses are balanced.
{[(])} - Parentheses are NOT balanced.

Output
    • For each test case, print on a new line "YES" if the parentheses are balanced.
    • Otherwise, print "NO"
"""
from collections import deque

parenthesis = deque(list(input()))
opened = deque()
sequence = '{[('
balance_couple = ['{}', '[]', '()']
balanced = True

while parenthesis:
    curr_par = parenthesis.popleft()
    if curr_par in sequence:
        opened.append(curr_par)
    elif not opened:
        balanced = False
        break
    elif opened.pop() + curr_par not in balance_couple:
        balanced = False
        break

if balanced:
    print('YES')
else:
    print('NO')
