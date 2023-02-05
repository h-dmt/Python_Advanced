
############################################################################################################
# Main colors: "red", "yellow", "blue"                                                                     #
# Secondary colors: "orange", "purple", "green"                                                            #
# To form a color, you should concatenate the first and the last substrings and check if                   #
# you can get any of the above colors' names. If there is only one substring left, you should              #
# use it to do the same check.                                                                             #
# You can only keep a secondary color if the two main colors needed for its creation could be              #
# formed from the given substrings:                                                                        #
#     • orange = red + yellow                                                                              #
#     • purple = red + blue                                                                                #
#     • green = yellow + blue                                                                              #
# Note: You could find some of the main colors needed to keep a secondary color after it is found.         #
# When you form a color, remove both substrings. Otherwise, you should remove the last character of        #
# each substring and return them in the middle of the original string.                                     #
# If the string contains an odd number of substrings, you should put the substrings one position ahead.    #
############################################################################################################

from collections import deque

main_colors = {'red', 'yellow', 'blue'}
secondary_colors_set = {'orange', 'purple', 'green'}
secondary_colors = {'orange': {'red', 'yellow'},
                    'purple': {'red', 'blue'},
                    'green': {'yellow', 'blue'}
                    }

colors_input = deque(w for w in input().split())
valid_colors = []
found_main = []
found_secondary = []

while colors_input:
    first = colors_input.popleft()
    if colors_input:
        last = colors_input.pop()
    else:
        last = ''
    mid_idx = int(len(colors_input)/2) if len(colors_input) % 2 == 0 else int(len(colors_input)//2 + 1)
    combo = {first + last, last + first}
    # match = combo & main_colors
    if combo & main_colors:
        valid_colors.append(''.join(combo & main_colors))
    elif combo & secondary_colors_set:
        valid_colors.append(''.join(combo & secondary_colors_set))
    else:
        first = first[:len(first)-1]
        last = last[:len(last)-1]
        if len(first) > 0:
            colors_input.insert(mid_idx, first)
        if len(last) > 0:
            colors_input.insert(mid_idx, last)

for color in valid_colors:
    if color in secondary_colors:
        if secondary_colors[color] == secondary_colors[color] & set(valid_colors):
            continue
        else:
            valid_colors.remove(color)
print(valid_colors)
