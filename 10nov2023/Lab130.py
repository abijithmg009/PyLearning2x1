#Method overloading
#Python will not support method overloading in the traditional way
#same name function with different paremeter, which was possible in JAVA



class MathUtil:
    def add(self, a, b):
        return a+b
    def add(self, a=0, b = 0 , c=0): #pass the default value
      return a+b+c


math = MathUtil()
op1 = math.add(1,2)
op2 = math.add(1,2,3)
op3 = math.add(1)
op4 = math.add()
print(op1)
print(op2)
print(op3)
print(op4)

#Method overloading is not possible in Python.