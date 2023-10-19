# Research What is Fibonacci series and Factorial.
"""
Fibonacci series - Fibonacci sequence is a sequence in which each number is the sum of the two preceding ones.

Numbers that are part of the Fibonacci sequence are known as Fibonacci numbers, commonly denoted Fn

Factorial Series - s the product of all positive integers less than or equal to
n! = n*(n-1)*(n-2).......3*2*1
"""

#Factorial

n= int(input("Enter the number\n"))
list = []
for i in range(n,0,-1):
    list.append(i)

print(list)

fact = 1

for x in list:
    fact = fact*x

print(f"factorial of {n} is {fact}")


#Fibonacci

n = int(input("Enter the number of fibonacci series \n"))
a= 0
b = 1
c = 1

print("Fibonacci Series:", a, b, end=" ")

for i in range(2, n):
    n3 = a + b
    print(n3, end=" ")
    a = b
    b = n3

print("\n")


#Example using break to exit a loop when i == 51 while printing the values from 1 to 100

for i in range(1,101):
    print(i, end=" ")
    if i==51:
        break
print("\n")
print("print stopped")

