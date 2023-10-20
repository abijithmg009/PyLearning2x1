#Fibinocci series

number = int(input("Enter the number\n"))

a = 0 #multiple initilization, a,b = 0,1
b = 1
#print(a,b)

while a<number:
    print(a, end= " ")
    a,b = b, a+b

