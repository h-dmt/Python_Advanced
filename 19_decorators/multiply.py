def multiply(n_times):
    def decorator(func):
        def wrapper(n):
            res = func(n) * n_times
            return res
        return wrapper
    return decorator


@multiply(3)
def add_ten(number):
    return number + 10


print(add_ten(3))
print()


@multiply(5)
def add_ten(number):
    return number + 10


print(add_ten(6))
