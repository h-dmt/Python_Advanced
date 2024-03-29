class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= self.number:
            raise StopIteration

        self.i += 1
        return self.sequence[(self.i-1) % len(self.sequence)]


result = sequence_repeat('I Love Python', 27)
for item in result:
    print(item, end ='')

print()

result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')