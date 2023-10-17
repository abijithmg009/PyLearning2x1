# maximum of 3 numbers

a = float(input("Enter the first number\n"))
b = float(input("Enter the second number\n"))
c = float(input("Enter the third number\n"))

if a > b and a > c:
    max = a
elif b > a and b > c:
    max = b
else:
    max = c

print(max)
