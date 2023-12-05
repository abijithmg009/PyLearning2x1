#Hybrid Level inhertence
# Multiple type of inheritence, such as single, multple, multilevel as well

class A:
    def methodA(self):
        return "Method A"
class B(A):
    def methodB(self):
        return "Method B"
class C(A):
    def methodC(self):
        return "Method C"
class D(B,C):
    def methodD(self):
        return "Method D"


d = D()
print(d.methodD())
print(d.methodA())
print(d.methodB())
print(d.methodC())
