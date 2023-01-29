"""You will receive a number N. On the following N lines, you will be receiving names. 
You should sum the ASCII values of each letter in the name and integer divide it by the number 
of the current row (starting from 1). Save the result to a set of either odd or even numbers, 
depending on if the resulting number is odd or even. After that, sum the values of each set.
    • If the sums of the two sets are equal, print the union of the values, separated by ", ".
    • If the sum of the odd numbers is bigger than the sum of the even numbers, print the different values, 
    separated by ", ".
    • If the sum of the even numbers is bigger than the sum of the odd numbers, 
    print the symmetric-different values, separated by ", "
"""

set_odd = set()
set_even = set()

for n in range(1, int(input()) + 1):
    letter_sum = sum([ord(i) for i in input()]) // n
    if letter_sum % 2 == 0:
        set_even.add(letter_sum)
    else:
        set_odd.add(letter_sum)
even_tot = sum(set_even)
odd_tot = sum(set_odd)

if even_tot == odd_tot:
    print(*(set_odd | set_even), sep=', ')
elif odd_tot > even_tot:
    print(*(set_odd - set_even), sep=', ')
elif even_tot > odd_tot:
    print(*(set_odd ^ set_even), sep=', ')
