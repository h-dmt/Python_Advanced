def fibonacci():
    n1, n2 = 0, 1

    while True:
        yield n1
        n1, n2 = n2, n1 + n2


generator = fibonacci()
for i in range(50):
    print(next(generator), end=' ')

print()

generator = fibonacci()
for i in range(1):
    print(next(generator))


# 0 1 1 2 3 5 8 13 ...
