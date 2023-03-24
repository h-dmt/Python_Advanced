def squares(n: int):
    i = 1
    while i < n + 1:
        yield i**2
        i += 1


print(list(squares(5)))
