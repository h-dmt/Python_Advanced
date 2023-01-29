"""
Write a program that finds the longest intersection. You will be given a number N.
On each of the next N lines you will be given two ranges in the format:
"{first_start},{first_end}-{second_start},{second_end}". You should find the intersection of these two ranges.
The start and end numbers in the ranges are inclusive.
Finally, you should find the longest intersection of all N intersections,
print the numbers that are included and its length in the format: "Longest intersection is
[{longest_intersection_numbers}] with length {length_longest_intersection}"
"""
intersection = set()
for _ in range(int(input())):
    first_range, second_range = input().split('-')
    start_a, end_a = list(map(int, first_range.split(',')))
    start_b, end_b = list(map(int, second_range.split(',')))
    set_A = set(i for i in range(start_a, end_a+1))
    set_B = set(i for i in range(start_b, end_b+1))
    new_intersection = set_A & set_B
    if len(new_intersection) > len(intersection):
        intersection = new_intersection
print(f"Longest intersection is {[x for x in intersection]} with length {len(intersection)}")
