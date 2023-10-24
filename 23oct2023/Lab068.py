digit = 12345
mod = digit % 10
print(mod)

num = int(input("Enter your number\n"))
sum = 0

while (num != 0):
    digit = num % 10
    sum = sum + digit
    num = int(num / 10)  # num//=10

print(sum)
