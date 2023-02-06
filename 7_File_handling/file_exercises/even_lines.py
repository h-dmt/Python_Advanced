# Write a program that reads a text file and prints on the console its even lines.
# Line numbers start from 0. Before you print the result, replace {"-", ",", ".", "!", "?"} with "@"
# and reverse the order of the words.

symbols = ["-", ",", ".", "!", "?"]
"""
with open("text.txt", 'w') as text_file:
    text_file.write("-I was quick to judge him, but it wasn't his fault.\n"
                    "-Is this some kind of joke?! Is it?\n"
                    "-Quick, hide here. It is safer.")

"""

with open("text.txt", "r") as text_file:
    lines = text_file.readlines()
for n in range(0, len(lines), 2):
    for symbol in symbols:
        lines[n] = lines[n].replace(symbol, '@')
    lines[n] = lines[n].split()[::-1]
    print(' '.join(lines[n]))

