def vowel_filter(function):

    def wrapper():

        VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')
        letters = function()
        output_vowels = []
        for let in letters:
            if let.lower() in VOWELS:
                output_vowels.append(let)

        return output_vowels
    return wrapper


@vowel_filter
def get_letters():
    return ["A", "b", "c", "d", "e"]

print(get_letters())
