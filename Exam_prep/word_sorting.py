# https://judge.softuni.org/Contests/Practice/Index/3430#2

def words_sorting(*words):
    words_dct = {}
    output_print = []
    tot_sum = 0
    for word in words:
        words_dct[word] = 0
        for char in word:
            words_dct[word] += ord(char)
            tot_sum += ord(char)

    if tot_sum % 2 == 0:  # sort values in ascending order, if the sum of all values of the dictionary is even
        words_dct = dict(sorted(words_dct.items(), key=lambda x: x[0]))
    else:  # values in descending order, if the sum of all values of the dictionary is odd
        words_dct = dict(sorted(words_dct.items(), key=lambda x: -x[1]))

    for key in words_dct:
        output_print.append(f"{key} - {words_dct[key]}")

    return '\n'.join(output_print)


print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
  ))
print()
print(
    words_sorting(
        'escape',
        'charm',
        'eye'
  ))
print()
print(
    words_sorting(
        'cacophony',
        'accolade'
  ))