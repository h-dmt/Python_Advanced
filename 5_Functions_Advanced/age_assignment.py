# print(age_assignment("Peter", "George", G=26, P=19))
# George is 26 years old.
# Peter is 19 years old.

def age_assignment(*names, **ages):
    names_print = []
    for letter in ages:
        for name in names:
            if name.startswith(letter):
                names_print.append(f"{name} is {ages[letter]} years old.")
    return '\n'.join(sorted(names_print))


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))