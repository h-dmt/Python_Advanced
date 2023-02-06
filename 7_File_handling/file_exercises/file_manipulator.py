# Until the command "End". The commands can be:
#     • "Create-{file_name}" - Creates the given file with an empty content. If the file already exists,
#     remove the existing text in it (as if the file is created again)
#     • "Add-{file_name}-{content}" - Append the content and a new line after it.
#     If the file does not exist, create it, and add the content
#     • "Replace-{file_name}-{old_string}-{new_string}" - Open the file and replace all the occurrences of the
#     old string with the new string. If the file does not exist, print: "An error occurred"
#     • "Delete-{file_name}" - Delete the file. If the file does not exist, print: "An error occurred"
from os.path import exists
from os import remove


def create_file(file_name):
    file = open(file_name, 'w')
    file.close()


def add_to_file(file_name, file_content):
    with open(file_name, 'a') as file:
        file.write(file_content + '\n')


def replace_file(file_name, old_str, new_str):
    try:
        if exists(file_name):
            with open(file_name, 'r') as file:
                lines = file.read()
            with open(file_name, 'w') as f:
                lines = lines.replace(old_str, new_str)
                f.write(lines)
    except FileExistsError:
        print("An error occurred")


def delete_file(file_name):
    try:
        remove(file_name)
    except FileNotFoundError:
        print("An error occurred")


while True:
    command = input().split('-')
    if command[0] == 'End':
        break
    elif command[0] == 'Create':
        name = command[1]
        create_file(name)
    elif command[0] == 'Add':
        name, content = command[1:]
        add_to_file(name, content)
    elif command[0] == 'Replace':
        name, old, new = command[1:]
        replace_file(name, old, new)
    elif command[0] == 'Delete':
        name = command[1]
        delete_file(name)
