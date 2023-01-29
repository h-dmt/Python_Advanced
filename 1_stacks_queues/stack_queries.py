"""
You will receive an integer – N. On the next N lines, you will
receive queries. Each query is one of these four types:

'1 {number}' – push the number (integer) into the stack
'2' – delete the number at the top of the stack
'3' – print the maximum number in the stack
'4' – print the minimum number in the stack
It is guaranteed that each query is valid.
After you go through all the queries, print the stack from top to bottom in the following
format:
"{n}, {n1}, {n2}, ... {nn}"
"""


def push_n(n, stackk):
    stackk.append(n)
    return stackk


def delete(stackk):
    if stackk:
        stackk.pop()
    return stackk


def print_max(stackk):
    max_n = -1000000
    if stackk:
        for num in stackk:
            if num >= max_n:
                max_n = num
        return max_n
    else:
        return ''


def print_min(stackk):
    min_n = 1000000
    if stackk:
        for num in stackk:
            if num <= min_n:
                min_n = num
        return min_n
    else:
        return ''


queries = int(input())
stack_n = list()
for q in range(queries):
    command = (input())
    if command.startswith('1'):
        command = command.split(' ')
        n = int(command[1])
        # print(n)
        stack = push_n(n, stack_n)
    elif command == '2':
        stack_n = delete(stack_n)
    elif command == '3':
        print(print_max(stack_n))
    elif command == '4':
        print(print_min(stack_n))

stack_n = list(map(str, stack_n))
reverse_n = list()
while stack_n:
    reverse_n.append(stack_n.pop())
print(', '.join(reverse_n))
