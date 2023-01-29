# Create your own exception called ValueCannotBeNegative.
# Write a program that reads five numbers from the console (on separate lines).
# If a negative number occurs, raise the exception.
class ValueCannotBeNegative(Exception):
    pass


numbers = []
for i in range(5):
    n = int(input())
    if n >= 0:
        numbers.append(n)
    else:
        raise ValueCannotBeNegative

print(numbers)
