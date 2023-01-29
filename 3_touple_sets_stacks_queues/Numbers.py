"""
First, you will be given two sequences of integers values on different lines.
The values of the sequences are separated by a single space between them.
Keep in mind that each sequence should contain only unique values.
Next, you will receive a number - N. On the next N lines, you will receive one of
the following commands:
    • "Add First {numbers, separated by a space}" - add the given numbers
    at the end of the first sequence of numbers.
    • "Add Second {numbers, separated by a space}" - add the given numbers
    at the end of the second sequence of numbers.
    • "Remove First {numbers, separated by a space}" - remove only the numbers
    contained in the first sequence.
    • "Remove Second {numbers, separated by a space}" - remove only the numbers
    contained in the second sequence.
    • "Check Subset" - check if any of the given sequences are a subset of the other.
    If it is, print "True". Otherwise, print "False".
In the end, print the final sequences, separated by a comma and a space ", ".
The values in each sequence should be sorted in ascending order.
"""

first = {int(x) for x in input().split()}
second = {int(x) for x in input().split()}

commands = {
    "Add First": lambda x: [first.add(el) for el in x],
    "Add Second": lambda x: [second.add(el) for el in x],
    "Remove First": lambda x: [first.discard(el) for el in x],
    "Remove Second": lambda x: [second.discard(el) for el in x],
    "Check Subset": lambda: [print(True) if first.issubset(second) or second.issubset(first) else print(False)]
}

for _ in range(int(input())):
    line_inp = input().split()
    command = ' '.join(line_inp[0:2])
    if len(line_inp) > 2:
        nums = {int(i) for i in line_inp[2:]}
        commands[command]([int(i) for i in nums])
    else:
        commands[command]()

print(*sorted(first), sep=', ')
print(*sorted(second), sep=', ')
