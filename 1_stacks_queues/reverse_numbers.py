"""
Write a program that reads a string with N integers from the console, separated by a single
space, and reverses them using a stack. Print the reversed integers on one line,
separated by a single space.
"""

stack_n = list(input().split())
while stack_n:
    print(stack_n.pop(-1), end=' ')
