# Write a program that reads a list of words from the file words.txt and finds how many times
# each of the words is contained in another file text.txt. Matching should be case-insensitive.
# The results should be written to other text files. Sort the words by frequency in descending order.

with open('words.txt', 'w') as w_file:
    w_file.write('quick is fault')

with open('input.txt', 'w') as input_f:
    input_f.write("-I was quick to judge him, but it wasn t his fault.\n"
                  "-Is this some kind of joke?! Is it?\n"
                  "-Quick, hide here… It is safer.")


with open('words.txt', 'r') as f:
    data = f.readline().split()

dct_words = {}
read_f = open('input.txt', 'r')
read_txt = read_f.read().split()
#print(read_txt)
for word in data:
    dct_words[word] = 0
    for w in read_txt:
        if w.strip('-,.').upper() == word.upper():
            dct_words[word] += 1

read_f.close()
dct_words = dict(sorted(dct_words.items(), key=lambda x: -x[1]))

for k, i in dct_words.items():
    print(f"{k} - {i}", sep='\n')
