import os
try:
    os.remove("/home/cris/Documents/Python SoftUni/Advanced/Exercises/7_File_handling/my_first_file.txt")
except FileNotFoundError:
    print('File already deleted!')

