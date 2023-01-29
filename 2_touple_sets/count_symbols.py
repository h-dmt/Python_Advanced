"""
Write a program that reads a text from the console and counts the occurrences of each character in it.
Print the results in alphabetical (lexicographical) order.
"""

a_text = sorted(tuple(input()))
counter = {k: a_text.count(k) for k in a_text}
for k, v in counter.items():
    print(f"{k}: {v} time/s", sep='\n')
