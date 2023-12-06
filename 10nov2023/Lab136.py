a = int(input("Enter the A number \n"))
b = int(input("Enter the B number \n"))

try:
    c = a / b
    print (c)
except Exception as Error:
    print("You're dividing by zero which is not possible",Error)