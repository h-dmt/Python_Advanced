class countdown_iterator:
    def __init__(self, count: int):
        self.count = count
        self.res = count + 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.res <= 0:
            raise StopIteration
        self.res -= 1

        return self.res


iterator = countdown_iterator(0)
for item in iterator:
    print(item, end=" ")