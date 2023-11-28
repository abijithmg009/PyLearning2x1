num = 20

def multiplyby10(n):
    n = n*10
    num = n #value will be changed inside function, fucntion scope
    print("Value inside fucntion",num)
    return n


out = multiplyby10(num)
print(out)
print("Value outside fucntion",num)
