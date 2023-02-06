# Create a program that opens the file.
# If the file is found, print 'File found'.
# If the file is not found, print 'File not found'.
# text.txt
# This is some random line
# This is the second line
# And this is the third one

try:
    text_file = open("text.txt", 'w')
    print('File found')
except FileNotFoundError:
    print('File not found')
