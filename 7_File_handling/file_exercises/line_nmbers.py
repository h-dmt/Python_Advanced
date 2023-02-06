# Write a program that reads a text file, inserts line numbers in front of each line, and counts all
# the letters and punctuation marks. The result should be written to another text file.

punctuation = ['-', '!', '?', ',', '.', ':', ';', "'"]
with open("text.txt", "r") as text_file:
    txt = text_file.readlines()
chars = 0
puncts = 0
with open('output.txt', 'w') as out_file:
    for i in range(len(txt)):
        line = txt[i]
        for ch in line:
            if ch.isalpha():
                chars += 1
            elif ch in punctuation:
                puncts += 1
        line = line.strip('\n') + ' ' + f"({chars})({puncts})"
        chars = 0
        puncts = 0
        out_file.write(f"Line {i + 1}: {line}\n")
"""
with open('output.txt', 'r') as output_file:
    print(output_file.read())
"""