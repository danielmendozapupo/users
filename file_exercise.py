#!/usr/bin/env python3.6

file_name = input('Enter the filename: ')
#open a file
file = open(file_name,'w')
print("Ready to write the content to the file...")
content = input()

if True:
    while content != '':
        file.write(content+'\n')
        content = input()
file.seek(0)
file.close()

with open(file_name, "r") as infile:  # open file for reading
    contents = infile.read()
print("Printing the content of the file\n")
print(contents)

