with open('../16oct2023/read.txt', 'r') as file:
    content = file.read()
    print(content)

with open('../16oct2023/read.txt', 'r') as file:
    line = file.readline()
    print(line)
#only first line is getting printed if we call readline, only 1 line it wil read and if we use readlines it will read
#all line in a list format, we can use a for format to make it lines

with open('/Users/abijithmg/PycharmProjects/PyLearning1x/16oct2023/read.txt', 'r') as file:
    lines = file.readlines()
    print(lines)
for l in lines:
    print(l, end='')


