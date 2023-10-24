#Lambda
#Anonious function\
#normal function


def SayHello():
    print("Hello")

SayHello()

def fucwithexp(a):
    return a**2
o = fucwithexp(2)
print(o)


#convert to lambda

output = lambda a:a**2
print(output(4))


sayHello = lambda name:print("hello",name)
sayHello("Pramod")