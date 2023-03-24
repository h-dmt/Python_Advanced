class reverse_iter:
    def __init__(self, iter_n: []):
        self.iter_n = iter_n[::-1]
        self.current = 0
        self.stop = len(self.iter_n) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.stop:
            result = self.iter_n[self.current]
            self.current += 1
            return result
        else:
            raise StopIteration


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)