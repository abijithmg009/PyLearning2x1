#Exceptions - are very easy in Python, not like Java

a = 10
b = 0

#print(a/b)
#Exceptions is an event that occurs that disturb the execution of normal flow of program


try:
    c = a/b
except ZeroDivisionError as error:
    print(error)