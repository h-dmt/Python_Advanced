# Write a program to flatten several lists of numbers received in the following format:
#     • String with numbers or empty strings separated by "|"
#     • Values are separated by spaces (" ", one or several)
#     • Order the output list from the last to the first matrix sub-lists
#     and their values from left to right as shown below
#       1 2 3 |4 5 6 |  7  88

nums = input().split('|')
M = [list(map(int, m.split())) for m in nums]

for r in range(len(M)-1, -1, -1):
    if M[r]:
        print(*M[r], end=' ')
