# Create a program that reads the numbers from the file.
# Print on the console the sum of those numbers.

num_file = open('numbers.txt', 'r')

sum = 0

for n in num_file:
    sum += int(n)
print(sum)
