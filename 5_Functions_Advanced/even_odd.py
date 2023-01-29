# Create a function called even_odd() that can receive a different quantity of numbers
# and a command at the end. The command can be "even" or "odd".
# Filter the numbers depending on the command and return them in a list.
# Submit only the function in the judge system.

def even_odd(*args):
    command = args[-1]
    result = []
    for n in args[:-1]:
        if int(n) % 2 == 0 and command == "even":
            result.append(n)
        elif int(n) % 2 != 0 and command == "odd":
            result.append(n)
    return result


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
