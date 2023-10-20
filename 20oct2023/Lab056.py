#Factorial:


n = int(input("Enter a number\n"))

if n<0:
    print("Factorial is not possible")
else:
    fact = 1
    for i in range(1, n+1):
        fact = fact*i

print("Factorial is ", fact)

