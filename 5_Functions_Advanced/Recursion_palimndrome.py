# Write a recursive function called palindrome() that will receive a word and an index (always 0).
# Implement the function, so it returns "{word} is a palindrome" if the word is a palindrome and
# "{word} is not a palindrome" if the word is not a palindrome using recursion.
# Submit only the function in the judge system.


def palindrome(word, i):

    if word[i] != word[-i-1]:
        return f"{word} is not a palindrome"
    elif i == len(word)//2:
        return f"{word} is a palindrome"
    i += 1
    return palindrome(word, i)



print(palindrome("huah", 0))
print(palindrome("peter", 0))
