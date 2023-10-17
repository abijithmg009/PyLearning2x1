# find the maximum of 3 numbers

num1 = float(input("Enter the first number\n"))
num2 = float(input("Enter the second number\n"))
num3 = float(input("Enter the third number\n"))

max_number = num1 if (num1>num2 and num1>num3) else (num2 if num2>num3 else num3)
print(f"the max number is {max_number}")
