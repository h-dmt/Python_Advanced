def get_primes(*args):
    prime = True

    for n in args[0]:
        for div in range(2, n):
            if n % div == 0:
                prime = False
                break
        if prime and n > 0 and n != 1 and n != 0:
            yield n

        prime = True


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
print()
print(list(get_primes([-2, 0, 0, 1, 1, 0])))
