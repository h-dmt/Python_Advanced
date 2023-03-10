"""
You will be given two sequences of characters, representing vowels and consonants.
Your task is to start checking if the following words could be found:
    • "rose"
    • "tulip"
    • "lotus"
    • "daffodil"
Start by taking the first character of the vowels collection and the last character from the consonants collection.
Then check if these letters are present in one or more of the given words. If a letter is present, that part of the
word is considered found. The word is gradually revealed with each letter found. Continue processing the next couple
of letters until you find one of the given words above.
A letter (vowels or consonants) could participate in more than one word or more than one time in a word,
for example:
    • The letter "o" is present in "rose", "lotus", and "daffodil".
    • The letter "l" is present in "tulip", "lotus", and "daffodil".
    • The letter "f" is present in the word "daffodil" twice.
The consonant and the vowel are always removed from the collection after trying to match them with the letters in
the given words (whether successful or not). In the end, the program stops when a word is found, or there are no
more vowels or consonants.
As a result, if you found a word, print it and the remaining letters in each collection in the format
described below.
Otherwise, print "Cannot find any word!" on the first line and t
he remaining letters in each sequence in the format described below.

    • On the first line:
        ◦ If a word is found, print it in the format: "Word found: {word_found}"
        ◦ Otherwise, print: "Cannot find any word!"
    • On the next lines, print the remaining letters in each collection (if there are any left):
        ◦ "Vowels left: {vowel_one} {vowel_two} … {vowel_N}"
        ◦ "Consonants left: {consonants_one} {consonants_two} … {consonants_N}"

"""

from collections import deque

vowels = deque(input().split())  # start by checking from the first
consonant = deque(input().split())  # start by checking from last
words = ['rose', 'tulip', 'lotus', 'daffodil']
matches = set()
match = False
while vowels and consonant and not match:
    v = vowels.popleft()
    c = consonant.pop()
    for word in words:
        if v in word:
            matches.add(v)
        if c in word:
            matches.add(c)
        if matches and not set(word) - matches:
            print(f"Word found: {word}")
            match = True

if not match:
    print("Cannot find any word!")
if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonant:
    print(f"Consonants left: {' '.join(consonant)}")
