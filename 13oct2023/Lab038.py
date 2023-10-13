#Task for 13th oct
# 1. Explain the difference between the = operator and the == operator in Python.
"""
== is comparision operator where = is assignment operator
Comparison operator which will compare the leftside is equal to right side of equeation eg : 5 == 5
Assigment operator will asssign the value on left side to rightside variable name, eg x=5
"""
a = 5
b = 6
print(a==b) #will return false as it is not equal

a = 6# will assign new value to variable a
print(a==b) #will be true as we have assigned new value to a

#2. What does the ** operator do in Python, and how is it used?
'''
** refers to exponential operator
if we write 2**3 = 2*2*2 = 8
'''
print(2**3)

#3What does the ^ operator do in Python, and in what context is it commonly used?
"""
The ^ operator compares each bit and set it to 1 if only one is 1, otherwise (if both are 1 or both are 0) it is set to 0
Takes two numbers as operands and does XOR on every bit of two numbers. The result of XOR is 1 if the two bits are different.

"""
a = 10
b = 7
print(a^b)


#Task 2

#1 - Write a Python program to calculate the area of a circle given its radius using the formula area=π×r^2 ( Take pie as 3.14)

r = float(input("Enter the radius of circle\n"))
pi = 3.14
area = pi*(r**2)
print(f"The area of circle is {area}")

#2Create a program that takes two numbers as input and prints whether the first number
# is greater than, less than, or equal to the second number.

a = input("Enter first number\n")
b = input("Enter second number\n")
print("Numbers are equal" if a==b else "The first number is greater than second" if a>b else"The second number is "
                                                                                            "greater than first")
#Use the ternary operator to find the maximum of three numbers entered by the user.
x = int(input("Enter the first number\n"))
y = int(input("Enter the second number\n"))
z = int(input("Enter the third number\n"))
max_value = x if(x>y and x>z) else (y if y>z else z)
print(f"The maximum value is {max_value}")

#Develop a Python script that calculates the square and cube of a given number.

num = int(input("enter the number\n"))
square = num**2
cube = num**3
print(f"The square of number is{square}")
print(f"The cube of number is {cube}")
