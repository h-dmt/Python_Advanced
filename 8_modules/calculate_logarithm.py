"""
    • On the first line, you will receive the number (an integer)
    • On the second line, you will receive a number, which is the logarithm base.
    It can be either a number or the word "natural"
The output should be formatted to the 2nd decimal digit
"""

from math import log

x = int(input("enter argument:\n"))
base = input("select the base, 'natural' or a number:\n")
if base.lstrip('-').isnumeric():
    exponent = log(x, int(base))
else:
    exponent = log(x)
print(f"{exponent: .2f}")
