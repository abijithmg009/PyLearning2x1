
#Capitalize
#Return a copy of string with it's First Character capital
name = "abijith"
#Strings are immutable in nature, they can't be created - new one will be created
#name[0] = "h", 'str' object does not support item assignment, string once created cannot be changed
result = name.capitalize()
print(result)

#Upper case
result2 = name.upper()
print(result2)
print(id(result2))
#id fucntions return the identity of the string.

#Lower
name3 = "ABIJITH"
print(name3.lower())

#Swapcase
#Return a copy, lower->capital and capital-> lower
name4 = "AbIjItH"
print(name4.swapcase())

#Title, Return a capitalized version
name = "hello world this is python"
print(name.title())

#name is variable name, hello world which is stored in memory

#lenth
print(len(name))

#Replace
text = "hello world"
result_replace = text.replace("world", "python")
print(result_replace)

#find
#returns the lowest index of substring found
text = "hello world"
index = text.find("world")
print(index)


#count
#count the number of character in the string
count = text.count("l")
print(count)


