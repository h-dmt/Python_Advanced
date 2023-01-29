"""
Write program that:
 Reads an input string
 Reverses it using a stack
 Prints the result back on the console
"""

random_string = list(input())

while random_string:
    print(random_string.pop(), end='')
