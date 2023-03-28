def type_check(a_type):
    def decorator(func):
        def wrapper(elem):
            if not isinstance(elem, a_type):
                return "Bad Type"

            return func(elem)
        return wrapper

    return decorator


@type_check(int)
def times2(num):
    return num*2


@type_check(str)
def first_letter(word):
    return word[0]


print(times2(2))
print(times2('Not A Number'))
print()
print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))