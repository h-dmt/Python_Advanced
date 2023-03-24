class custom_range:
    def __init__(self, start: int, stop: int):
        self.current = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.stop:
            result = self.current
            self.current += 1
            return result

        else:
            raise StopIteration


one_to_ten = custom_range(1, 10)
for num in one_to_ten:
    print(num)