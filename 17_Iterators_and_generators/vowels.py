class vowels:
    def __init__(self, in_list: str):
        self.vowels = vowels
        self.start_i = 0
        self.in_list = in_list
        self.vouels_list = ['a', 'e', 'i', 'o', 'u', 'y']
        self.vowels = [ch for ch in self.in_list if ch.lower() in self.vouels_list]
        self.end_i = len(self.vowels) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.start_i <= self.end_i:
            res = self.vowels[self.start_i]
            self.start_i += 1
            return res
        else:
            raise StopIteration


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
