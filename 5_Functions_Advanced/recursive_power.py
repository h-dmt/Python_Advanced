def recursive_power(n, p):
    if n == 0 and p == 0:
        return 'Undetermined'
    if p == 1:
        return n
    elif p == 0:
        return 1
    return n*recursive_power(n, p-1)

print(recursive_power(3, -3))

"""if p < 0:
    if p == -1:
        return 1 / n
    return n * recursive_power(n, p + 1)
"""