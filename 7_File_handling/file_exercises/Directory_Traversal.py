# Write a program that traverses a given directory for all files.
# Search through the first level of the directory only and write information about each found file in report.txt.
# The files should be grouped by their extension. Extensions should be ordered by name alphabetically.
# The files with extensions should also be sorted by name. report.txt should be saved in the chosen directory.

import os


def show_directory_content(path, first_level=False):
    list_directory = os.listdir(path)
    # print(list_directory)
    for file in list_directory:
        f = os.path.join(path, file)
        if os.path.isfile(f):
            ext = '.' + file.split('.')[-1]
            if ext not in content:
                content[ext] = [file]
            else:
                content[ext].append(file)
        elif os.path.isdir(f) and not first_level:
            path = os.path.join(path, file)
            show_directory_content(path, first_level=True)


content = dict()
path = "/home/cris/Documents/Python SoftUni/Advanced/Exercises/7_File_handling/"
show_directory_content(path)
content = dict(sorted(content.items(), key=lambda x: (x[0], x[1])))

for extension in content:
    print(extension)
    for file in content[extension]:
        print(f"- - - {file}")
