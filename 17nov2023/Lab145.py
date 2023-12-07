# File handling
# how to read file and write into it using python code

#open a file
#   file_object = open("Abijith.txt", mode=)
#    'r' for reading mode which is default one
#    'w' for writing (create a new file or truncates an existing one
#    'a' for appending
#    'b' for binary mode
#    '+' for updating (reading or writing)

# Read a file
# read entire content : content = file.object.read()
#line = file_object.readline() for a single line
#lines = file_object.readlines() for all lines in list

# write to a file
#writing string : file_object.write(string)
#writing multiple lines : file_object.writelines(list of strings)

# closing the file
#file_object.close()

"""
write will replace and append will add lines

"""

try:
    with open("TestData2.txt", 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError as error:
    print(error)

