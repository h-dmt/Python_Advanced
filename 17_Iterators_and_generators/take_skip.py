class take_skip:
    def __init__(self, step: int, count: int):
        self.count = count
        self.step = step
        self.res = - self.step
        self.iter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.iter >= self.count:
            raise StopIteration

        self.res += self.step
        self.iter += 1
        return self.res


numbers = take_skip(10, 5)
for number in numbers:
    print(number)

numbers = take_skip(2, 6)
for number in numbers:
    print(number)