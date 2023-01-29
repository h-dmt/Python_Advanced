# Write a concatenate() function that receives some strings as arguments
# and some named arguments (the key will be a string, and the value will be another string).
# First, you should concatenate all arguments successively. Next, take each key successively,
# and if it is present in the resulted string, change all matching parts with the key's value.
# In the end, return the final string.

def concatenate(*args, **kwargs):
    text = ''.join(args)

    for k in kwargs:
        text = text.replace(k, kwargs[k])
    return text



print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))
print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))