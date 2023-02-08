"""
    • "Create Sequence {count}". Create a series of numbers up to a specific count and
    print them in the following format:
           "{n1} {n2} … {n}"

    • "Locate {number}"
            Check if the sequence contains the number. If it finds the number, it should print:
            "The number - {number} is at index {index}"
             And if it doesn't find it:
            "The number {number} is not in the sequence"
"""


def create_sequence(count):
    global sequence
    sequence = [0]
    if count == 0:
        print(sequence)
    sequence = [0, 1]
    for i in range(2, count):
        sequence.append(sequence[i-1] + sequence[i-2])
    print(*sequence)


def locate(number):
    for ind, n in enumerate(sequence):
        if n == number:
            return f"The number - {number} is at index {ind}"

    return f"The number {number} is not in the sequence"

