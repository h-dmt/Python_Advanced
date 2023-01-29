"""
You are given an algebraic expression with parentheses. Scan through the string and
extract each set of parentheses.
Print the result back on the console.
"""

expression = input()
index_open = []
for i in range(len(expression)):
    if expression[i] == '(':
        index_open.append(i)
    elif expression[i] == ')':
        closed_i = i
        print(expression[index_open[-1]:closed_i+1])
        index_open.pop()

