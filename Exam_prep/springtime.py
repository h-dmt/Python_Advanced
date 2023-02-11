"""
Write a function called start_spring which will receive a different number of keyword arguments.
Each keyword holds a key with a name of the spring object (string), and each value holds its type (string).
For example, dahlia="flower", shrikes="bird", dogwood="tree".
The function should sort the given spring objects in collections by their type:

    • The collections sorted by their number of elements in descending order.
        If two or more collections have the same number of elements in them,
    return them in ascending order (alphabetically) by the type's name.
    • Each collection's elements should be sorted in ascending order (alphabetically) by the object's name.
"""


def start_spring(**kwargs):
    return_string = []
    type_dict = {}
    for k, v in kwargs.items():
        if v not in type_dict:
            type_dict[v] = [k]
        else:
            type_dict[v].append(k)

    #  sorting by numbers of elements per key in descending order and ascending key name
    type_dict_sorted = dict(sorted(type_dict.items(), key=lambda x: (-len(x[1]), x[0])))

    #  formatting the output
    for k in type_dict_sorted:
        return_string.append(f"{k}:")
        for value in sorted(type_dict_sorted[k]):  # sorting the values in ascending order
            return_string.append(f"-{value}")
    return '\n'.join(return_string)


example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))