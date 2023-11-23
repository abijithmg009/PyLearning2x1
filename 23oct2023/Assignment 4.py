"""
✅ Create a Lambda expression to triple power 2**3 a number

"""

triple=lambda num : num**3

num=int(input("Enter number : "))

print(f'Cube of {num} is : {triple(num)}')