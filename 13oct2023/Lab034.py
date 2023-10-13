#Identity operator

# is return  True if both values are the same object
# is not  return True if both values are not the same object


x = [1,2,3]
y = [1,2,3]

print(x is y)
print(x is not y)

print(id(x))
print(id(y))


a = 10
b = 10

print(a is b)
print(a is not b)

print(id(a))
print(id(b))

# here the identity is same that is the reason the is return true on above list it is showing different variableName
# is and is not usually used with list, Dict and Tuples during operator

