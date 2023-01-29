# Write a function called multiply that can receive any quantity of numbers (integers) as
# different parameters and returns the result of the multiplication of all of them.
# Submit only your function in the Judge system.

def multiply(*args):
    result = 1
    for n in args:
        result *= n
    return result


print(multiply(5, 4, 7, 1))
