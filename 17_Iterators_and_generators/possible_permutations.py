from itertools import permutations


def possible_permutations(in_lst):
    for el in permutations(in_lst):
        yield list(el)


[print(n) for n in possible_permutations([1, 2, 3])]