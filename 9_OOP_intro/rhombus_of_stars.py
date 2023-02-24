# A program that reads a positive integer N as input and prints on the console a rhombus
# with size n:

class Rhombus:
    def __init__(self, n: int):
        self.n = n
        self.outprint = []

        def create_figure():
            row = 1
            lower_part = False

            while row > 0:
                self.outprint.append(f"{' ' * (self.n - row)}{'* ' * row}")
                if row == self.n:
                    lower_part = True
                row = row - 1 if lower_part else (row + 1)

        create_figure()

    def __repr__(self):
        return "\n".join(self.outprint)


rhomb = Rhombus(int(input()))
print(rhomb)
